class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            left = nums[l]
            right = nums[r]
            mid = nums[m]

            if mid > right:
                l = m + 1
            else:
                r = m

        if target <= nums[-1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0

        print(f"l: {l}, r: {r}")
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1