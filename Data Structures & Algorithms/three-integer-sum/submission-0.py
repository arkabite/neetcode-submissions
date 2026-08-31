class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,v in enumerate(nums):
            if i>0 and nums[i-1]==v:
                continue
            
            l,r=i+1,len(nums)-1
            while l<r:
                val=v+nums[l]+nums[r]
                if val>0:
                    r-=1
                elif val<0:
                    l+=1
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res