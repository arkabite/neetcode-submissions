class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prod=nums[0]
        for i in range(1,len(nums)):
            res[i]=res[i]*prod
            prod*=nums[i]
        
        prod=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i]=res[i]*prod
            prod*=nums[i]
        
        return res