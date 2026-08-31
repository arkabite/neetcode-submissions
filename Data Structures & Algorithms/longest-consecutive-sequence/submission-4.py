class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        n=len(nums)
        res=0
        for i in nums:
            length=0
            if (i-1) in sett:
                continue
            
            while (i+length) in sett:
                length+=1
            
            res=max(res,length)
        return res