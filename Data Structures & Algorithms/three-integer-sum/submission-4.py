class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i,v in enumerate(nums):
            if v==nums[i-1] and i>0:
                continue

            l=i+1
            r=n-1
            while l<r:
                target=v+nums[l]+nums[r]
                if target<0:
                    l+=1
                elif target>0:
                    r-=1
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

                