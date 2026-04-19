class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for course, pre in prerequisites:
            if pre in adjList:
                adjList[pre].append(course)
            else:
                adjList[pre] = [course]
        safe = set()
        def dfs(node, visited):
            if node in visited:
                return False
            if node in safe:
                return True
            visited.add(node)
            safe.add(node)
            if node not in adjList:
                return True
            for adj in adjList[node]:
                if not dfs(adj, visited):
                    return False
            return True

        for i in range(numCourses):
            visited = set()
            if not dfs(i, visited):
                return False
        return True
        