class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prod1=1
        prod2=1
        for i in range(n-1):  
            prod1*=nums[i]
            res[i+1]=prod1

        for j in range(n-1,0,-1):
            prod2*=nums[j]
            res[j-1]*=prod2
        
        return res
