class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            
            # Left sorted portion
            if nums[l]<=nums[m]:
                if target>nums[m]:
                    l=m+1
                elif target<nums[l]:
                    l=m+1
                else:
                    r=m-1
            else:
            #right sorted portion
                if target<nums[m]:
                    r=m-1
                elif target>nums[r]:
                    r=m-1
                else:
                    l=m+1

                    

        return -1