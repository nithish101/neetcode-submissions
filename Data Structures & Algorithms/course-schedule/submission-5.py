class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            pre[a].append(b)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for b in pre[course]:
                if not dfs(b):
                    return False
            visited.remove(course)
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
            