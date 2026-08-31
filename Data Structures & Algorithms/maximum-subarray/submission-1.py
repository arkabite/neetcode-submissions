class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        for i in range(len(nums)):
            val=nums[i]
            res=max(res,val)
            for j in range(i+1,len(nums)):
                val+=nums[j]
                res=max(res,val)
        return res