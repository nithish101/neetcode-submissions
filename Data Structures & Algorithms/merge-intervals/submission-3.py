class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda pair : pair[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = res[-1]
            s2, e2 = intervals[i]
            if s2 <= e:
                res[-1] = [min(s, s2), max(e, e2)]
            else:
                res.append(intervals[i])

        return res