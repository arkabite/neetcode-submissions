class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prod=nums[0]
        for i in range(1,len(nums)):
            res[i]=res[i]*prod
            prod*=nums[i]
        
        prod=nums[-1]
        for j in range(n-2,-1,-1):
            res[j]=res[j]*prod
            prod*=nums[j]
        
        return res