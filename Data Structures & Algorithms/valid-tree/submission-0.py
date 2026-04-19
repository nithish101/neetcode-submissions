class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set([0])

        def dfs(node, parent):
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
            