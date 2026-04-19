"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s, e = 0, 0
        count, maxCount = 0, 0

        while s < len(intervals) and e < len(intervals):
            if ends[e] <= starts[s]:
                e += 1
                count -= 1
            else:
                s += 1
                count += 1
                maxCount = max(maxCount, count)
        
        return maxCount