class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod=nums[0]
        res=[1]*n
        for i in range(1,n):
            res[i]=res[i]*prod
            prod*=nums[i]
        
        prod=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i]=res[i]*prod
            prod*=nums[i]
        
        return res