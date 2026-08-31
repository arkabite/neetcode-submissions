class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def dfs(i):
            if i>=len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            robFirst=nums[i]+dfs(i+2)
            skipFirst=dfs(i+1)
            memo[i]=max(robFirst,skipFirst)
            return memo[i]
        
        return dfs(0)