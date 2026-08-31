class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prod=nums[0]
        for i in range(1,n):
            res[i]*=prod
            prod*=nums[i]
        
        prod=nums[-1]
        for i in range(n-2,-1,-1):
            res[i]*=prod
            prod*=nums[i]
        
        return res