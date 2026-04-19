class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            midIndex = l + (r - l) // 2
            left = nums[l]
            right = nums[r]
            mid = nums[midIndex]
            print(mid)
            
            if mid > right:
                l = midIndex + 1
            else:
                r = midIndex
        return nums[l]