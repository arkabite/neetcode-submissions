class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda item:item[0])
        res=[]
        res.append(intervals[0])
        for start,end in intervals[1:]:
            val=res[-1][1]
            if start<=val:
                res[-1][1]=max(val,end)
            else:
                res.append([start,end])
                
        return res