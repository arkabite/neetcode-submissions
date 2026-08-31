class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for i,v in enumerate(nums):
            if nums[i-1]==v and i>0:
                continue
            
            left=i+1
            right=n-1
            while left<right:
                value=v+nums[left]+nums[right]
                if value>0:
                    right-=1
                elif value<0:
                    left+=1
                else:
                    res.append([v,nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    
        return res