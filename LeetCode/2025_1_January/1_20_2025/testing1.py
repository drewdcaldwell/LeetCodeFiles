def firstCompleteIndex(arr, mat):
    numRows = len(mat)
    print("Num Rows")
    print(numRows)
    numCols = len(mat[0])
    print("Num Cols")
    print(numCols)
    flatGrid = []
    for row in mat:
        flatGrid += row
    rowCount = [0]*numRows
    colCount = [0]*numCols
    for i in arr:
        rowCount[(flatGrid.index(i)) % numRows] += 1
        colCount[(flatGrid.index(i)) % numCols] += 1
        print(rowCount)
        print(colCount)
        if rowCount[(flatGrid.index(i)) % (numRows)] == numRows or colCount[(flatGrid.index(i)) % (numCols)] == numCols:
            print("MATCH")
            return arr.index(i)


arr = [8,2,3,5,6,7,4,1,9,10]
mat = [[6,9],[7,4],[1,10],[3,8],[2,5]]
print(firstCompleteIndex(arr, mat))
