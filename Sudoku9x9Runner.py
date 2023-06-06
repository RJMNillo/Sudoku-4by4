from Sudoku9x9 import SudoSquare
import time
import random

def Sudo9Solver(square):
    Square = SudoSquare(square)
    Square.printSquare()
    while(Square.checkEmpty()):
        print("There are some empty spaces left")
        Square.checkAvailabilityMatrix()
        if(Square.CheckBlocks()):
            print("Program can't go any further...")
            break
        # TightlyAvailableNumber = min(min(Square.Availability_Matrix))
        # print(str(TightlyAvailableNumber))
        # With this minimum, we can do a random lookup and add a number from there
        somex = random.randint(0,8)
        somey = random.randint(0,8)
        # AvailableNumber = Square.Availability_Matrix[somey][somex]
        # while AvailableNumber > TightlyAvailableNumber:
            # somex = random.randint(0,8)
            # somey = random.randint(0,8)
            # AvailableNumber = Square.Availability_Matrix[somey][somex]
        print(f"We are looking at {somex},{somey}")

        # Next, We can now use this 
        Square.PutNumber(somex,somey)

        Square.printSquare()

if __name__ == "__main__":
    begin = time.time()
    ASquare = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]

    Sudo9Solver(ASquare)
    end = time.time()

    print(f"Time Elapsed: {end - begin}")

