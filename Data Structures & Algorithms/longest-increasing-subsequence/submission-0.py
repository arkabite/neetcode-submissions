class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        memo={}

        def dfs(i):
            if i==len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            maxLen=1

            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    maxLen=max(maxLen,1+dfs(j))
            memo[i]=maxLen
            return memo[i]
        
        overallMax=float("-inf")

        for i in range(len(nums)):
            overallMax=max(overallMax,dfs(i))

        
        return overallMax