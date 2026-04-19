class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda pair : pair[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i]
            oldStart, oldEnd = res[-1]

            if newStart <= oldEnd:
                res[-1][1] = max(newEnd, oldEnd)
            else:
                res.append(intervals[i])

        return res
