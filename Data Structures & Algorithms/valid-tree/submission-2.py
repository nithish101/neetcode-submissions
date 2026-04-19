class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nb in adjList[node]:
                if nb == parent:
                    continue
                if not dfs(nb, node):
                    return False
            return True
        return dfs(0, None) and len(visited) == n