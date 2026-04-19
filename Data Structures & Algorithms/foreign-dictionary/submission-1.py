class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        result = []

        for i in range(len(words) - 1):
            j = 0
            minLength = min(len(words[i]), len(words[i + 1]))
            while j < minLength and words[i + 1][j] == words[i][j]:
                j += 1
            if j >= minLength:
                if len(words[i + 1]) < len(words[i]):
                    return ""
            else:
                adj[words[i][j]].add(words[i + 1][j])

        visited = {} # False if visiting, True if visited

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = False
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visited[c] = True
            result.append(c)
            return True
            

        for c in adj:
            if not dfs(c):
                return ""
        return "".join(result[::-1])