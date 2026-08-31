class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        res=0
        for i in nums:
            if (i-1) in sett:
                continue
            depth=0
            while (i+depth) in sett:
                depth+=1
            res=max(res,depth)
        return res