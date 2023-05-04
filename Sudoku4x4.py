import random

# a class for the Sudoku Square
class SudoSquare:
    def __init__(self, othersquare = None):
        # A square in sudoku
        self.Square =[
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

        # If a person has a sudoku square in mind, they can put it in
        if othersquare is not None:
            self.Square = othersquare

        # Said Square's Availability Matrix
        self.Availability_Matrix = [
            [4,4,4,4],
            [4,4,4,4],
            [4,4,4,4],
            [4,4,4,4]
        ]

    # Helper Functions
    def printSquare(self):
        for x in range(0,4):
            print(self.Square[x])
    
    # Print the Matrix
    def printMatrix(self):
        for x in range(0,4):
            print(self.Availability_Matrix[x])
    
    # Check if there are any empty slots
    def checkEmpty(self):
        EmptySquares = False
        for y in range(0, len(self.Square)):
            for x in range(0, len(self.Square[y])):
                if self.Square[y][x] == 0:
                    EmptySquares = True
        
        return EmptySquares
    
    # checkSubsqare: Find what square your selection is at
    # This only works with 4x4 squares
    def checkSubsquare(self,x,y):
        if y < 2:
            if x < 2:
                return ("A00")
            else:
                return ("A01")
        else:
            if x < 2:
                return ("A10")
            else:
                return ("A11")
    
    # Check Availability Matrix
    def checkAvailabilityMatrix(self):
        for y in range(0, len(self.Square)):
            for x in range(0,len(self.Square[y])):
                # Is the square filled already?
                if self.Square[y][x] > 0:
                    # Set its matrix to 99
                    # So that value isn't considered for min
                    self.Availability_Matrix[y][x] = 99
                else:
                    self.checkAvailableNumbers(y, x)
        print("Availability matrix:")
        self.printMatrix()
    
    # Look for available numbers in the Square itself
    def checkAvailableNumbers(self, y, x):
        AvailableNumbers = [1,2,3,4]
        # check rows
        for row in range(0, len(self.Square)):
            if self.Square[row][x] > 0:
                if self.Square[row][x] in AvailableNumbers:
                    AvailableNumbers.remove(self.Square[row][x])
        # check columns
        for col in range(0, len(self.Square)):
            if self.Square[y][col] > 0:
                if self.Square[y][col] in AvailableNumbers:
                    AvailableNumbers.remove(self.Square[y][col])
        # Check subsquare
        self.checkSubSquareNumber(self.checkSubsquare(x,y),AvailableNumbers)

        # Update the availability matrix
        self.Availability_Matrix[y][x] = len(AvailableNumbers)
    
    # Check subsquare based on the number being processed
    def checkSubSquareNumber(self, text, availabilitylist):
        # Check the text
        if text == "A00":
            for y in range(0, 2):
                for x in range(0,2):
                    if self.Square[y][x] > 0:
                        if self.Square[y][x] in availabilitylist:
                            availabilitylist.remove(self.Square[y][x])
        elif text == "A01":
            for y in range(0, 2):
                for x in range(2,4):
                    if self.Square[y][x] > 0:
                        if self.Square[y][x] in availabilitylist:
                            availabilitylist.remove(self.Square[y][x])
        elif text == "A10":
            for y in range(2, 4):
                for x in range(0,2):
                    if self.Square[y][x] > 0:
                        if self.Square[y][x] in availabilitylist:
                            availabilitylist.remove(self.Square[y][x])
        else:
            for y in range(2, 4):
                for x in range(2,4):
                    if self.Square[y][x] > 0:
                        if self.Square[y][x] in availabilitylist:
                            availabilitylist.remove(self.Square[y][x])
    
    # Check the Availability Matrix
    def CheckBlocks(self):
        isBlocked = False
        for y in range(0, len(self.Availability_Matrix)):
            for x in range(0, len(self.Availability_Matrix[y])):
                if self.Availability_Matrix[y][x] == 0:
                    isBlocked = True
        return isBlocked

    # Fill in the number
    def PutNumber(self, x, y):
        AvailableNumbers = [1,2,3,4]
        # check rows
        for row in range(0, len(self.Square)):
            if self.Square[row][x] > 0:
                if self.Square[row][x] in AvailableNumbers:
                    AvailableNumbers.remove(self.Square[row][x])
        # check columns
        for col in range(0, len(self.Square)):
            if self.Square[y][col] > 0:
                if self.Square[y][col] in AvailableNumbers:
                    AvailableNumbers.remove(self.Square[y][col])
        # Check subsquare
        self.checkSubSquareNumber(self.checkSubsquare(x,y),AvailableNumbers)

        # use random guess to put in the number
        if len(AvailableNumbers) > 0:
            self.Square[y][x] = random.choice(AvailableNumbers)



# Main Function
if __name__ == "__main__":
    Square = SudoSquare()
    Square.printSquare()
    while(Square.checkEmpty()):
        print("There are some empty spaces left")
        Square.checkAvailabilityMatrix()
        TightlyAvailableNumber = min(min(Square.Availability_Matrix))
        # print(str(TightlyAvailableNumber))
        # With this minimum, we can do a random lookup and add a number from there
        somex = random.randint(0,3)
        somey = random.randint(0,3)
        AvailableNumber = Square.Availability_Matrix[somey][somex]
        while AvailableNumber > TightlyAvailableNumber:
            somex = random.randint(0,3)
            somey = random.randint(0,3)
            AvailableNumber = Square.Availability_Matrix[somey][somex]
        print(f"We are looking at {somex},{somey}")

        # Next, We can now use this 
        Square.PutNumber(somex,somey)

        Square.printSquare()
