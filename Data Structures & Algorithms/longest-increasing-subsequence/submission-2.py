class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        answer = 0
        for i, num in enumerate(nums):
            longest = 1
            for j in range(i):
                if num > nums[j]:
                    longest = max(longest, dp[j] + 1)
            dp[i] = longest
            answer = max(answer, longest)

        return answer