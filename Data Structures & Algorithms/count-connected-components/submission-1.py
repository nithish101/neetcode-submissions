class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()
        print(adjList)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count