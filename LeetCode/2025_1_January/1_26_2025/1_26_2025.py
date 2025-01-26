#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
# 2127     DCALDWELL   1/26/25   Maximum Employees to Be     #
#                                Invited to a Meeting        #
#------------------------------------------------------------#

class Solution(object):
    def maximumInvitations(self, favorite):
        
        n = len(favorite)
        visited = [False]*n
        indegrees = [0]*n
        for node in favorite:
            indegrees[node]+=1
        
        from collections import deque
        que = deque()
        for i in range(n):
          if indegrees[i]==0:
             que.append(i)
        while que:
            o = que.popleft()
            visited[o]=True
            indegrees[favorite[o]]-=1
            if indegrees[favorite[o]]==0:
                que.append(favorite[o])

        ## forming a reverse adjacency matrix for tails
        rev = [[] for i in range(n)]
        for i in range(n):
            rev[favorite[i]].append(i)
        
        def dfs(n, exclude):
            stack = [(0,n)]
            max_height=0
            while stack:
                h, node=stack.pop()
                flag = False
                for c in rev[node]:
                    if c!= exclude:
                        flag = True
                        stack.append((h+1, c))
                if flag:
                    max_height=max(max_height, h+1)
            return max_height
            

        compo_with_cy2=0
        max_big_cycle = 0
        for i in range(n):
            if not visited[i]:## a cycle
               if favorite[favorite[i]]==i: ## cycle with 2
                  visited[i] = True
                  visited[favorite[i]]= True
                  compo_with_cy2+= 2+dfs(i, favorite[i])+dfs(favorite[i], i)
               else: ## cycle with more than 2 
                  c = 1
                  j= i
                  visited[j] = True
                  while favorite[j]!=i:
                    j = favorite[j]
                    visited[j] = True
                    c+=1
                  max_big_cycle = max(max_big_cycle, c)

        return max(max_big_cycle, compo_with_cy2)

                

        
