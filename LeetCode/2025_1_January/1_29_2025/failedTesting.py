def findRedundantConnection(edges):
    n = len(edges)
    visited = set()
    saveEdges = []
    count = 0
    for i in edges:
        if i[0] in visited and i[1] in visited:
            saveEdges.append(i)
        if i[0] or i[1] not in visited:
            visited.add(i[0])
            visited.add(i[1])
        count += 1
        if count == n:
            return saveEdges[0]
        

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
edges = [[1,2],[1,3],[2,3]]
edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
print(findRedundantConnection(edges))
# Output: [1,4]
