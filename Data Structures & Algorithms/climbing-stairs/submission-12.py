class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i==n:
                return 1

            if i>n:
                return 0

            val=dfs(i+1)+dfs(i+2)
            memo[i]=val
            return memo[i]
        
        return dfs(0)

