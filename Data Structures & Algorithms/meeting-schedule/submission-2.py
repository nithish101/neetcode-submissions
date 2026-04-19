"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval : interval.start)
        finalTime = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start < finalTime:
                return False
            finalTime = max(finalTime, end)
        return True