"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        i, j = 0, 0
        count, max_count = 0, 0

        while i < len(intervals):
            if ends[j] <= starts[i]:
                j += 1
                count -= 1
            else:
                count += 1
                i += 1
                max_count = max(max_count, count)

        return max_count