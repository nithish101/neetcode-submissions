class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            count = 1
            if (num - 1) not in numSet:
                curr = num + 1
                while curr in numSet:
                    count += 1
                    curr += 1

            longest = max(longest, count)

        return longest
