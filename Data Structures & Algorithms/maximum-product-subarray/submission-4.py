class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]

        for l in range(len(nums)):
            prod=1
            for r in range(l,len(nums)):
                prod*=nums[r]
                res=max(res,prod)
        
        return res