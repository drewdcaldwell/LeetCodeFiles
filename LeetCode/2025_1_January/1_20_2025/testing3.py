def firstCompleteIndex(arr, mat):
    numRows = len(mat)
    numCols = len(mat[0])
    print("==NUMROWS==")
    print(numRows)
    print("==NUMCols==")
    print(numCols)
    unfoldedGrid = []
    for row in mat:
        unfoldedGrid += row
    rowCount = [0]*numRows
    colCount = [0]*numCols
    print(unfoldedGrid)
    
    for i in arr:
        #print(unfoldedGrid.index(i))
        rowCount[(unfoldedGrid.index(i)) % numRows] += 1
        #print((unfoldedGrid.index(i)) % rowFreq)
        colCount[(unfoldedGrid.index(i)) % numCols] += 1
        print("==ROW COUNT==")
        print(rowCount)
        print("==COL COUNT==")
        print(colCount)
        if rowCount[(unfoldedGrid.index(i)) % (numRows)] == numCols or colCount[(unfoldedGrid.index(i)) % (numCols)] == numRows:
            #print("Match")
            #print(arr.index(i))
            return arr.index(i)
        
        
arr =[1,4,5,2,6,3]
mat =[[4,3,5],[1,2,6]]
#print(firstCompleteIndex(arr, mat))

#arr =[1,4,5,2,6,3]
#mat =[[4,3,5],[1,2,6]]
arr = [8,2,3,5,6,7,4,1,9,10]
mat = [[6,9],[7,4],[1,10],[3,8],[2,5]]
print(firstCompleteIndex(arr, mat))
