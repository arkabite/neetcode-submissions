class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        res=0
        for i,v in enumerate(heights):
            lastpop=i
            while stack and stack[-1][1]>v:
                indx,val=stack.pop()
                lastpop=indx
                res=max(res,(i-indx)*val)
            stack.append((lastpop,v))
        
        while stack:
            indx,val=stack.pop()
            res=max(res,(n-indx)*val)
        
        return res