#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
# 1368     DCALDWELL   1/20/25   Min Cost to make at least   #
#                                   one valid path on a grid #
#                                -HEAP                       #
#------------------------------------------------------------#

import heapq

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dist = [[1e9 for _ in range(n)] for _ in range(m)]  # Initialize distance matrix with large values
        vis = [[0 for _ in range(n)] for _ in range(m)]  # Initialize a visited matrix to keep track of visited cells
        dx = [0, 0, 0, 1, -1]  # Change in x-coordinate for different moves
        dy = [0, 1, -1, 0, 0]  # Change in y-coordinate for different moves
        pq = [(0, 0, 0)]  # Priority queue to store cost, x-coordinate, and y-coordinate

        dist[0][0] = 0  # Starting cell has cost 0

        while pq:
            cost, x, y = heapq.heappop(pq)  # Pop the cell with the minimum cost from the priority queue
            if vis[x][y]:  # If the cell has been visited already, skip it
                continue
            vis[x][y] = 1  # Mark the cell as visited

            for i in range(1, 5):  # Explore all possible moves
                x2, y2 = x + dx[i], y + dy[i]  # Calculate the new coordinates after the move
                if x2 < 0 or y2 < 0 or x2 >= m or y2 >= n:  # Check if the new coordinates are out of bounds
                    continue
                if grid[x][y] == i:  # If the cell specifies the same move, no additional cost
                    if dist[x2][y2] >= cost:
                        dist[x2][y2] = cost
                        heapq.heappush(pq, (cost, x2, y2))
                else:  # If the cell specifies a different move, add 1 to the cost
                    if dist[x2][y2] >= cost + 1:
                        dist[x2][y2] = cost + 1
                        heapq.heappush(pq, (cost + 1, x2, y2))

        return dist[m-1][n-1]  # Return the minimum cost to reach the bottom-right corner
