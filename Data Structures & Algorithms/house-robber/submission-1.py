class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def minidfs(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]

            val=nums[i]
            maxVal=0
            for j in range(i+2,len(nums)):
                maxVal=max(maxVal,minidfs(j))
            val=val+maxVal
            memo[i]=val
            return val
        
        for i in range(len(nums)):
            minidfs(i)
        
        res=0
        for i,v in memo.items():
            res=max(res,v)
        
        return res