class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        currMin = prices[0]
        for price in prices:
            best = max(best, price - currMin)
            currMin = min(currMin, price)
        return best
        