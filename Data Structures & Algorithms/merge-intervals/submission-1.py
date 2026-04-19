class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair : pair[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            if output[-1][1] >= newInterval[0]:
                output[-1][1] = max(output[-1][1], newInterval[1])
            else:
                output.append(newInterval)
        return output