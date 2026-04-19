class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for i in range(1, len(strs)):
            l = min(len(ans), len(strs[i]))
            new_ans = ""
            for j in range(l):
                if ans[j] == strs[i][j]:
                    new_ans += ans[j] 
                else:
                    ans = new_ans
                    break
            ans = new_ans

        return ans