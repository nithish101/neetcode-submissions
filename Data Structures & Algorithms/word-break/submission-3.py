class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for dw in wordDict:
                if (i - len(dw) >= 0 and dp[i - len(dw)]
                    and dw == s[i - len(dw) : i]):
                    dp[i] = True
                    continue
        print(dp)
        return dp[-1]