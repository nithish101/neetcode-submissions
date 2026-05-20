class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0 # most without i
        b = nums[0] # most with i

        for i in range(1, len(nums)):
            most = max(a + nums[i], b)
            a = b
            b = most

        return max(a, b)