class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = 0
        for i in range(1, len(nums) + 1):
            check = check ^ i
        for i in range(len(nums)):
            check = check ^ nums[i]
        return check