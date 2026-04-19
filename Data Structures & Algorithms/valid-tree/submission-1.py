class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()
        def dfs(node, parent):
            if node in visited: # cycle detected
                return False
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor != parent and not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n