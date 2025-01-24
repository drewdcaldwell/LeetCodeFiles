#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
#  802     DCALDWELL   1/24/25   Find Eventual Safe States   #
#------------------------------------------------------------#

class Solution:
    def eventualSafeNodes(self, graph):
        n=len(graph)
        safe={}
        ans=[]
        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i]=False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]

            safe[i]=True
            return safe[i]

        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans         
