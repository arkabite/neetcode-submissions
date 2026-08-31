class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n=len(height)
        l=0
        r=n-1
        maxL=height[0]
        maxR=height[-1]
        res=0 
        while l<r:
            val=0
            if maxL<=maxR:
                l+=1
                maxL=max(maxL,height[l])
                res+=maxL-height[l]
            else:
                r-=1
                maxR=max(maxR,height[r])
                res+=maxR-height[r]
        
        return res

