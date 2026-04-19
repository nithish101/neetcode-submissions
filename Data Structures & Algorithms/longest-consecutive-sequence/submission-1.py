class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        numSet = set(nums)
        seqLength = {} # last num in sequence -> len(seq)
        for num in nums:
            if (num - 1) not in numSet:
                seqLength[num] = 1

        for num in seqLength.keys():
            curr = num + 1
            while curr in numSet:
                seqLength[num] += 1
                curr += 1

        return max(seqLength.values())
