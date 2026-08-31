class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        res=0
        for i in nums:
            if (i-1) in sett:
                continue
            
            length=0
            while (i+length) in sett:
                length+=1
            res=max(res,length)
        
        return res