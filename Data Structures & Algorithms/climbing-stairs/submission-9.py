class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}

        def dfs(i):
            if i>n:
                return 0
            if i==n:
                return 1
            if i in memo:
                return memo[i]
            
            val=dfs(i+1) + dfs(i+2)
            memo[i]=val
            return memo[i]
        
        return dfs(0)