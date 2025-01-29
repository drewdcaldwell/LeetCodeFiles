# So close. Unfortunately test cases are killing me

class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        visited = set()
        count = 0
        for i in edges:
            if i[0] in visited and i[1] in visited:
                saveEdge = i
            if i[0] or i[1] not in visited:
                visited.add(i[0])
                visited.add(i[1])
            count += 1
            if count == n:
                return saveEdge
