class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        res=0
        for i in nums:
            if (i-1) in seen:
                continue
            length=1
            while (i+length) in seen:
                length+=1
            
            res=max(res,length)
        
        return res