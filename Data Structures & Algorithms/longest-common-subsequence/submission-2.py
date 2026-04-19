class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text1))] for i in range(len(text2))]

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if text1[j] == text2[i]:
                    dp[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] += dp[i - 1][j - 1]
                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
        
        print(dp)
        return dp[-1][-1]