"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res=[]
        prevMax=0
        for i in intervals:
            res.append([i.start,i.end])

        res.sort(key= lambda item:item[0])

        if len(res)==0:
            return True
            
        prevMax=res[0][1]
        for start,end in res[1:]:
            if start>=prevMax:
                prevMax=end
            else:
                return False

        return True
