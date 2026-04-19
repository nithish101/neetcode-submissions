class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            print(l, r)
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # left side
            if nums[m] >= nums[l]:
                if nums[m] < target:
                    l = m + 1
                    print(1)
                elif target < nums[l]:
                    l = m + 1
                    print(2)
                else:
                    r = m - 1
                    print(3)
            # right side
            else:
                if nums[m] > target:
                    r = m - 1
                    print(4)
                elif target > nums[r]:
                    r = m - 1
                    print(5)
                else:
                    l = m + 1
                    print(6)

        return -1