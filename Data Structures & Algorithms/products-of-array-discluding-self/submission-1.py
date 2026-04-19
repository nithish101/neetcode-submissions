class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProducts = [1] * len(nums)
        postProducts = [1] * len(nums)

        for i in range(1, len(nums)):
            preProducts[i] = preProducts[i - 1] * nums[i - 1]
            postProducts[len(nums) - 1 - i] = postProducts[len(nums) - i] * nums[len(nums) - i]

        output = []
        for i in range(len(nums)):
            output.append(preProducts[i] * postProducts[i])

        return output