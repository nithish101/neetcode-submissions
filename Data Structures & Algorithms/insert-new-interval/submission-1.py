class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newStart, newEnd = newInterval
        after = -1
        for i, (start, end) in enumerate(intervals):
            if newStart <= end:
                after = i
                break

        if after == -1:
            intervals.append(newInterval)
            return intervals
        
        start, end = intervals[after]
        if newEnd < start:
            intervals.insert(after, newInterval)
            return intervals

        before = after
        while after < len(intervals):
            if newEnd >= intervals[after][0]:
                after += 1
            else:
                break
        a = min(newStart, intervals[before][0])
        b = max(newEnd, intervals[after - 1][1])
        return intervals[0 : before] + [[a, b]] + intervals[after :]