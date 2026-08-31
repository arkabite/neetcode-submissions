class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
            
        def dfs(i,end,memo):
            if i>=end:
                return 0
            
            if i in memo:
                return memo[i]
            
            robCurrent=nums[i]+dfs(i+2,end,memo)
            skipCurrent=dfs(i+1,end,memo)

            val=max(robCurrent,skipCurrent)
            memo[i]=val
            return memo[i]
        
        robFirstHouse=dfs(0,len(nums)-1,{})
        robLastHouse=dfs(1,len(nums),{})

        return max(robFirstHouse,robLastHouse)