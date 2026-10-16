class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}

        def dfs(i):
            if i in memo:
                return memo[i]
                
            if i>n:
                return 0
            
            if i==n:
                return 1
            
            oneStep=dfs(i+1)
            twoStep=dfs(i+2)
            val=oneStep+twoStep
            memo[i]=val
            return memo[i]
        
        return dfs(0)
