class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if len(adj[course]) == 0:
                return True
            visiting.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            adj[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True