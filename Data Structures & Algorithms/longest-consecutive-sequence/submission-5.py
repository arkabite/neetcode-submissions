class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        sett=set(nums)
        res=1
        for i in nums:
            length=0
            if i-1 in sett:
                continue
            
            while (i+length) in sett:
                length+=1
            res=max(res,length)
        return res
