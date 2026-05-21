"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for i in intervals:
            heapq.heappush(starts, i.start)
            heapq.heappush(ends, i.end)

        maxRooms = 0
        currRooms = 0

        while len(starts) > 0:
            if ends[0] <= starts[0]:
                currRooms -= 1
                heapq.heappop(ends)
            else:
                currRooms += 1
                maxRooms = max(maxRooms, currRooms)
                heapq.heappop(starts)

        return maxRooms
