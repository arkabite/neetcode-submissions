class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        res=0
        l=0
        r=n-1
        while l<r:
            minHeight=min(heights[l],heights[r])
            vol=minHeight*(r-l)
            res=max(res,vol)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
