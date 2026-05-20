class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = [False for _ in range(n)]
        count = 0

        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in adjList[i]:
                dfs(j)

        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        
        return count