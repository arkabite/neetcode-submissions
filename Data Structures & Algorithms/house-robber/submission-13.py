class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i>=len(nums):
                return 0
            
            robfirst=dfs(i+1)
            robSecond=nums[i]+dfs(i+2)
            val=max(robfirst,robSecond)
            memo[i]=val
            return memo[i]
        
        return dfs(0)
