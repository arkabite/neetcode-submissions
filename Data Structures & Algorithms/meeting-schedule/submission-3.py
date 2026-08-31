"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda i:i.start)
        if len(intervals)==0:
            return True

        prevMax=0
        for i in intervals:
            if i.start>=prevMax:
                prevMax=i.end
            else:
                return False

        return True
