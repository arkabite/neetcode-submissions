class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i,v in enumerate(nums):
            if i>0 and v==nums[i-1]:
                continue
            
            l=i+1
            r=n-1
            while l<r:
                val=nums[l]+nums[r]+v
                if val>0:
                    r-=1
                elif val<0:
                    l+=1
                else:
                    res.append([nums[l],nums[r],v])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        
        return res