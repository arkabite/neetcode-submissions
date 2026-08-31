class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[0]
        if n==2:
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
        

        robFirst=dfs(0,n-1,{})
        robLast=dfs(1,n,{})

        return max(robFirst,robLast)