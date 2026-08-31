class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[0]*len(height)
        maxRight=[0]*len(height)
        res=0

        val=0
        for i in range(len(height)):
            maxLeft[i]=val
            val=max(val,height[i])
        
        val=0
        for i in range(len(height)-1,-1,-1):
            maxRight[i]=val
            val=max(val,height[i])
        
        print(maxLeft)
        print(maxRight)
        for i in range(len(height)):
            val=(min(maxLeft[i],maxRight[i])-height[i])
            if val>0:
                res+=val
        
        return res

            
