class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first, create graph, courses point to prereqs
        adjList = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adjList[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(course) -> bool:
            if course in visiting: # cycle found
                return False
            if course in visited: # already checked
                return True
            visiting.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True