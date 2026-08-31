class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count=nums.count(0)
        if count>1:
            return [0]*len(nums)
        elif count>0:
            res=[]
            prod=1
            for i in nums:
                if i!=0:
                    prod*=i
            for i in nums:
                if i==0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        
        prod=1
        res=[]
        for i in nums:
            prod*=i
        
        for i in nums:
            val=prod//i
            res.append(val)
        return res
            
            
