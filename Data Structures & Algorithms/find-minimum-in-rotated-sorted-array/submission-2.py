class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            print(l, mid, r)
            mid = (l + r) // 2
            if l == mid:
                return min(nums[r], nums[l])
            if nums[l] < nums[mid] and nums[mid] < nums[r]:
                return nums[l]
            elif nums[l] < nums[mid]:
                l = mid
                continue
            elif nums[l] > nums[mid] and nums[mid] < nums[r]:
                r = mid
        