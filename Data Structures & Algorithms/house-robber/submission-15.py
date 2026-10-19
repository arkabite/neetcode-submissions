class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i>=len(nums):
                return 0
            
            robFirst=nums[i]+dfs(i+2)
            robSecond=dfs(i+1)
            val=max(robFirst,robSecond)
            memo[i]=val
            return memo[i]

        return dfs(0)