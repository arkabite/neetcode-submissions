class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        n=len(heights)
        l=0
        r=n-1

        while l<r:
            h=min(heights[l],heights[r])
            vol=h*(r-l)
            res=max(res,vol)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        
        return res
            