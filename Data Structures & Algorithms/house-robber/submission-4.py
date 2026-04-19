class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = nums[0]
        for i in range(1, len(nums)):
            temp = curr
            curr = max(prev + nums[i], curr)
            prev = temp
        return max(prev, curr)
