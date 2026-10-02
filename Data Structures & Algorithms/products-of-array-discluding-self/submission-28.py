class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val=nums[0]
        prefix=[i for i in nums]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i]*val
            val=prefix[i]
        
        val=nums[-1]
        postfix=[i for i in nums]
        for i in range(len(nums)-2,-1,-1):
            postfix[i]=postfix[i]*val
            val=postfix[i]
        
        res=[1]*len(nums)
        for i in range(len(nums)):
            l=i-1
            r=i+1
            if l<0:
                lVal=1
                res[i]=lVal*postfix[r]
            elif r>=len(nums):
                rVal=1
                res[i]=prefix[l]*rVal
            else:
                res[i]=prefix[l]*postfix[r]
        
        return res
