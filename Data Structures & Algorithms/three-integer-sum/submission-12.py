class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i,v in enumerate(nums):
            if i>0 and nums[i-1]==v:
                continue
            l=i+1
            r=n-1
            while l<r:
                val=v+nums[l]+nums[r]
                
                if val>0:
                    r-=1
                elif val<0:
                    l+=1
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res

