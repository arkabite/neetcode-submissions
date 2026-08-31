class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        res=0
        while l<r:
            h=min(heights[l],heights[r])
            vol=h*(r-l)
            res=max(res,vol)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res