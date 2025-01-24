# I just cant win with these.
# Worked on the first 40 test cases.

class Solution(object):
    def eventualSafeNodes(self, graph):
        index = 0
        terminalNodes = []
        for i in graph:
            # print("Node: "+str(i)+ " || Length: " + str(len(i)) + " || Index: " +str(index))
            if len(i) == 0:
                terminalNodes.append(index)
            index += 1
        print(terminalNodes)
        index = 0
        for i in graph:
            count = 0
            for j in i:
                if j in terminalNodes:
                    count += 1
                if count == len(i):
                    terminalNodes.append(index)
            index += 1
        terminalNodes.sort()
        return terminalNodes
