class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            currArea = (r - l) * min(heights[l], heights[r])
            maximum = max(maximum, currArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maximum