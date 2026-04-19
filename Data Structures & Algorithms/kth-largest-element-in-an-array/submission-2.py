class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if p == k:
                return nums[p]
            elif k > p:
                return quickSelect(p + 1, r)
            elif k < p:
                return quickSelect(l, p - 1)

        return quickSelect(0, len(nums) - 1)