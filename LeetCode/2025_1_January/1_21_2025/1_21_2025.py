#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
# 2017     DCALDWELL   1/21/25   Grid Game                   #
#------------------------------------------------------------#

class Solution(object):
    def gridGame(self, grid):
        topSum = sum(grid[0])                      # Sum the top row
        botSum = 0                                 #Initialize the bottom row Sum
        min2 = float('inf')                        # initialize the min so that we grntee min
        for i in range(len(grid[0])):              #iterate over the columns
            topSum -= grid[0][i]                   # take away the current element from the top row
            min2 = min(min2, max(topSum, botSum))  # take the min of what is left of the topsum, botsum, 
                                                   # and our current min. This makes sure that we switch 
                                                   # to the bottom row at the correct time.
            botSum += grid[1][i]                   # Add to the bottom sum showing that we iterated over it
        return min2                                # return min2 :)
