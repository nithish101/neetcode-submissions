class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev = 0
        curr = 0
        for num in nums[:-1]:
            temp = curr
            curr = max(prev + num, curr)
            prev = temp
        
        max1 = curr

        prev = 0
        curr = 0
        for num in nums[1:]:
            temp = curr
            curr = max(prev + num, curr)
            prev = temp

        return max(max1, curr)