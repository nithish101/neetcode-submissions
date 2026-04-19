class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        canFlow = [[[False, False] for a in range(len(heights[0]))] for b in range(len(heights))]
        result = []
        

        def markPath(i, j, ocean):
            if i < 0 or i >= len(heights):
                return
            if j < 0 or j >= len(heights[i]):
                return
            if canFlow[i][j][ocean]:
                return
            canFlow[i][j][ocean] = True
            if canFlow[i][j][1 - ocean]:
                result.append([i, j])

            if i - 1 >= 0 and heights[i][j] <= heights[i - 1][j]:
                markPath(i - 1, j, ocean)
            if j - 1 >= 0 and heights[i][j] <= heights[i][j - 1]:
                markPath(i, j - 1, ocean)
            if i + 1 < len(heights) and heights[i][j] <= heights[i + 1][j]:
                markPath(i + 1, j, ocean)
            if j + 1 < len(heights[i]) and heights[i][j] <= heights[i][j + 1]:
                markPath(i, j + 1, ocean)
    
        i = 0
        for j in range(len(heights[0])):
            markPath(i, j, 0) # 0 is pacific

        i = len(heights) - 1
        for j in range(len(heights[0])):
            markPath(i, j, 1)

        j = 0
        for i in range(len(heights)):
            markPath(i, j, 0)

        j = len(heights[0]) - 1
        for i in range(len(heights)):
            markPath(i, j, 1)
        
        return result


        
