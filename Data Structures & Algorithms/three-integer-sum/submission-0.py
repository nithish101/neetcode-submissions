class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        for i in range(len(nums)):
            target = -1 * nums[i]
            hm = {}
            for j in range(len(nums)):
                if j == i:
                    continue
                if (target - nums[j]) in hm:
                    ret.add(tuple(sorted([nums[i], nums[j], target - nums[j]])))
                else:
                    hm[nums[j]] = j

        return [list(item) for item in ret]
                