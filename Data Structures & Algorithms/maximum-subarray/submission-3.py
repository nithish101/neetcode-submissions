class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 1
        currSum = nums[0]
        maxSum = currSum

        while r < len(nums):
            if currSum < 0:
                currSum = 0
            currSum += nums[r]
            maxSum = max(maxSum, currSum)
            

            r += 1
        return maxSum