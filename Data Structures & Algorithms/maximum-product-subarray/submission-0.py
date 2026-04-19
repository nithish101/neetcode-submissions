class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProduct = nums[0]
        maxProduct = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                minProduct, maxProduct = maxProduct, minProduct
            minProduct = min(minProduct * num, num)
            maxProduct = max(maxProduct * num, num)

            res = max(res, maxProduct)

        return res