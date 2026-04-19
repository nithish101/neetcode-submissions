class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda item : item[1])
        prevEnd = intervals[0][1]
        numRemoved = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                numRemoved += 1
            else:
                prevEnd = intervals[i][1]
        return numRemoved