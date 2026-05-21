class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = max(0, nums[0])

        for num in nums[1:]:
            curr += num
            best = max(best, curr)
            if curr < 0:
                curr = 0

        return best