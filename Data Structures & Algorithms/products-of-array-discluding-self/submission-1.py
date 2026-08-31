class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        res=[]
        n=len(nums)
        prod1=1
        prod2=1
        
        for i in range(n):
            prod1*=nums[i]
            prefix.append(prod1)
        
        for i in range(n-1,-1,-1):
            prod2*=nums[i]
            postfix.append(prod2)
        postfix=postfix[::-1]
        for i in range(n):
            val=1
            if i==0:
                val=1*postfix[i+1]
            elif i==n-1:
                val=prefix[i-1]*1
            else:
                val=prefix[i-1]*postfix[i+1]
            
            res.append(val)
        
        return res
