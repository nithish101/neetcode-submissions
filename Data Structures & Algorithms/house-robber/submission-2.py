class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        robPrev = 0
        robCurr = 0
        for num in nums:
            temp = robCurr
            robCurr = max(robPrev + num, robCurr)
            robPrev = temp
        return robCurr