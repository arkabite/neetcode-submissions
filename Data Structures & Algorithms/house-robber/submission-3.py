class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def dfs(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            robCurrent=nums[i]+dfs(i+2)
            skipCurrent=dfs(i+1)

            val=max(robCurrent,skipCurrent)
            memo[i]=val
            return memo[i]
        
        return dfs(0)