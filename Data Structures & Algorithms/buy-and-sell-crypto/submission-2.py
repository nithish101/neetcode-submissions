class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
            else:
                if prices[i] - currMin > ans:
                    ans = prices[i] - currMin

        return ans