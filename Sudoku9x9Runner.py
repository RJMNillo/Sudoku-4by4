from Sudoku9x9 import SudoSquare
import time
import random

def decisionmaker(square):
    WideAvailableNumber = max(max(square.Availability_Matrix))
    print(f"Widely Available Space: {WideAvailableNumber}")

    #Do a For loop to find this elusive number
    OneLeft = False
    for row in range(0, len(square.Availability_Matrix)):
        for col in range(0, len(square.Availability_Matrix[row])):
            if square.Availability_Matrix[row][col] == 1:
                OneLeft = True
                break

    if OneLeft:
        print("There is a slot where only one number can fit!")
        return 1
    else:
        print("Many more options are still available.")
        return WideAvailableNumber


def Sudo9Solver(square):
    Square = SudoSquare(square)
    Square.printSquare()
    while(Square.checkEmpty()):
        print("There are some empty spaces left")
        Square.checkAvailabilityMatrix()
        if(Square.CheckBlocks()):
            print("We're blocked. Removing num...")
            Square.removeNumber(somex,somey)
            continue
        DecidedNumber = decisionmaker(Square)
        # With this number, we can do a random lookup and add a number from there
        somex = random.randint(0,8)
        somey = random.randint(0,8)
        AvailableNumber = Square.Availability_Matrix[somey][somex]
        while AvailableNumber != DecidedNumber:
            somex = random.randint(0,8)
            somey = random.randint(0,8)
            AvailableNumber = Square.Availability_Matrix[somey][somex]
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

