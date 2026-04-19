class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        i = len(nums) - 2

        # set i to before strictly decreasing
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        if i >= 0:
            nI = i + 1
            for j in range(i + 2, len(nums)):
                if nums[j] > nums[i] and nums[j] < nums[nI]:
                    nI = j
            swap(i, nI)
        
        l = i + 1
        r = len(nums) - 1

        while l < r:
            swap(l, r)
            l += 1
            r -= 1