# 1769
#
class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        output = [0] * n
        for i in range(0,n):
            maxMoves = 0
            for j in range(0,n):
                if boxes[j] == "1":
                    maxMoves += abs(i-j)
            output[i] = maxMoves
            
        return output
        