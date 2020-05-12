#!/usr/bin/python
import sys # For reading from commandline
matrix = [] # Declaring global matrix list

def readMatrix():
    global matrix
    matrixRowSize=0
    file=open(sys.argv[1]) # Opens file from commandline
    while True:
        line = file.readline().strip() # Saves current line of file in line
        if not line : # end of file
            break
        if len(matrix) > 0:
            if len(line) != matrixRowSize:
                return False
        matrixRowSize = len(line)
        matrix.append(line.split(' ')) # Appends each number to the matrix array
    return True 

def diagonality():
    global matrix
    for x in range(0,len(matrix)): # Counts for each row
        for y in range(0,len(matrix[x])): # Counts for each Column
            if x != y:
                if int(matrix[x][y]) != 0:
                    return False
    return True

def scalar():
    global matrix
    scalarNum=int(matrix[0][0])
    for x in range(0,len(matrix)): # Counts for each row
        for y in range(0,len(matrix[x])): # Counts for each Column
            if x == y:
                if scalarNum != int(matrix[x][y]):
                    return False
            elif x != y:
                if int(matrix[x][y]) != 0:
                    return False
    return True

def nullMatrix():
    global matrix
    for x in range(0,len(matrix)): # Counts for each row
        for y in range(0,len(matrix[x])): # Counts for each Column
            if int(matrix[x][y])!=0:
                return False
    return True

def unit():
    global matrix
    for x in range(0,len(matrix)): # Counts for each row
        for y in range(0,len(matrix[x])): # Counts for each Column
            if x == y:
                if int(matrix[x][y]) != 1:
                    return
            elif x != y:
                if int(matrix[x][y]) != 0:
                    return
    print("This is a Unit Matrix of degree "+str(len(matrix)))
    return

def uTriangle():
    global matrix
    for x in range(0,len(matrix)): # Counts for each row
        for y in range(0,len(matrix[x])): # Counts for each Column
            if x > y:
                if int(matrix[x][y]) != 0:
                    return False
    return True

def lTriangle():
    global matrix
    for x in range(0,len(matrix)): # Counts for each row
        for y in range(0,len(matrix[x])): # Counts for each Column
            if x < y:
                if int(matrix[x][y]) != 0:
                    return False
    return True

def symmetric():
    global matrix
    matrixRange = 0
    for x in range(0,len(matrix)): # Counts for each row
        for y in range(matrixRange,len(matrix[x])): # Counts for each Column
            if x != y:
                if int(matrix[x][y]) != int(matrix[y][x]):
                    return False
            matrixRange += 1
    return True

def main():
    global matrix
    square=False
    if readMatrix() == False: # Validates matrix
        print("Error with Matrix")
        return
    else: # Matrix is Valid!
        # Test for matrix shape
        # Row Matrix
        if len(matrix) == 1:
            print("This is a Row Matrix")
        # Column Matrix
        if len(matrix[0]) == 1:
            print("This is a Column Matrix")
        # Square Matrix
        if len(matrix) == len(matrix[0]):
            print("This is a Square Matrix")
            square=True
        # Rectangle Matrix
        else:
            print("This is a Rectangle Matrix")
        
        # Check for diagonality and if scalar, and if unit matrix
        if square:
            if scalar():
                    print("This is a Scalar Matrix")
            elif diagonality():
                print("This is a Diagonal Matrix")
            unit()
        
        # Check if null
        if nullMatrix():
            print("This is a Null Matrix")

        # Check if upper Triangular Matrix
        if uTriangle():
            print("This is an Upper Triangular Matrix")
        # Check if lower Triangular Matrix
        if lTriangle():
            print("This is a Lower Triangular Matrix")

        # Symmetric Matrix
        if symmetric():
            print("This is a Symmetric Matrix")

    return

if __name__ == "__main__":
        main()