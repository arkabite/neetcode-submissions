class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda item:item[0])
        count=0
        res=[]
        res.append(intervals[0])
        for start,end in intervals[1:]:
            val=res[-1][1]
            if start>=val:
                res.append([start,end])
            else:
                res[-1][1]=min(val,end)
                count+=1
        return count