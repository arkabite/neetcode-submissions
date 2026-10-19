class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1={}
        memo2={}

        def dfs(i,memo,arr):
            if i in memo:
                return memo[i]
            
            if i>=len(arr):
                return 0
            
            robFirst=arr[i]+dfs(i+2,memo,arr)
            robSecond=dfs(i+1,memo,arr)
            val=max(robFirst,robSecond)
            memo[i]=val
            return memo[i]
        
        forbFirst=dfs(0,memo1,nums[1:])
        robLast=dfs(0,memo2,nums[:len(nums)-1])
        return max(forbFirst,robLast,nums[0])

        
