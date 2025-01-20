#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
# 2661     DCALDWELL   1/20/25   First Completely Painted Row# 
#                                or Column                    #
#------------------------------------------------------------#

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        # Define the length and height 
        m = len(mat)
        n = len(mat[0])
        # Initialize map
        map = {}
        # Create the mapping
        for i in range(m):
            for j in range(n):
                map[mat[i][j]] = [i, j]
        # Create count arrays
        row = [0] * m
        col = [0] * n
        # Iterate over arr until the row index or col index = m or n
        for i in range(len(arr)):
            x = map[arr[i]]
            row[x[0]] += 1
            col[x[1]] += 1
            if row[x[0]] == n or col[x[1]] == m:
                return i
        # If we get here something bad happened
        return -1
        
