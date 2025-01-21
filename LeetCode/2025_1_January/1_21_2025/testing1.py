# Worked on the first couple but couldnt get it to work since it is only Dijkstras

class Solution(object):
    def gridGame(self, grid):
        r = 0
        c = 0
        maxSum = 0
        grid[r][c] = 0
        while c != len(grid[r])-1:
            if r == len(grid)-1:
                # This means that we are on the last row and 
                # can only move to the right from now on.
                c += 1
                grid[r][c] = 0 # set the rest to 0
            else:
                if grid[r][c+1] >= grid[r+1][c]:
                    c += 1
                    grid[r][c] = 0
                else:
                    r += 1
                    grid[r][c] = 0
        for i in grid:
            currentSum = sum(i)
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum
