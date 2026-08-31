class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[0]
        
        if n==2:
            return max(nums[0],nums[1])
        
        def helper(l,r):
            rob1,rob2=0,0

            for i in range(l,r):
                temp=max(nums[i]+rob1,rob2)
                rob1=rob2
                rob2=temp
            
            return rob2
        
        robFirst=helper(0,n-1)
        robLast=helper(1,n)

        return max(robFirst,robLast)