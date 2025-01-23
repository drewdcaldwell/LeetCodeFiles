#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
#                                                            #
#------------------------------------------------------------#

class Solution(object):
    def countServers(self, grid):
        n = len(grid)                              # Get number of Rows
        m = len(grid[0])                           # Get the number of columns
        row = [0]*n                                # Initialize an array of the number of rows
        col = [0]*m                                # Initialize an array of the number of columns
        for i in range(n):                         # Iterate over all of grid and count the number of 1's that appear per row and column
            for j in range(m):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        ans = 0                                    # Initialize the output
        for i in range(n):
            for j in range(m):
                if (grid[i][j] and row[i] > 1):    # if the current grid spot is 1 and the row has more than 1 server
                    ans += 1                       # increase ans by 1
                elif (grid[i][j] and col[j] > 1):
                    ans += 1
        return ans
        
