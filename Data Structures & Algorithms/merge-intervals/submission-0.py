class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=intervals
        def helper(val,li):
            res=[]
            for i in range(len(li)):
                if val[1]<li[i][0]:
                    res.append(val)
                    return res+li[i:]
                elif val[0]>li[i][1]:
                    res.append(li[i])
                else:
                    val=[min(val[0],li[i][0]),max(val[1],li[i][1])]
            res.append(val)
            return res
        
        for i in intervals:
            res=helper(i,res)
        
        return res