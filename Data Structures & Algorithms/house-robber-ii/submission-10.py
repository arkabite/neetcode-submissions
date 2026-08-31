class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums[0],nums[1])
            
        def dfs(l,r,memo):
            if l>=r:
                return 0
            if l in memo:
                return memo[l]
            
            robCurrent=nums[l]+dfs(l+2,r,memo)
            skipCurrent=dfs(l+1,r,memo)

            val=max(robCurrent,skipCurrent)
            memo[l]=val
            return memo[l]
        
        robFirst=dfs(0,len(nums)-1,{})
        robLast=dfs(1,len(nums),{})
        return max(robFirst,robLast)