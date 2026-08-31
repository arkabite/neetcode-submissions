class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        res=nums[0]

        while l<=r:
            if nums[l]<nums[r]:
                res=min(res,nums[l])
            m=l+(r-l)//2
            val=nums[m]
            res=min(res,val)
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        
        return res