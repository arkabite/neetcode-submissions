class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        res=0
        for i in nums:
            if (i-1) in seen:
                continue
            
            depth=0
            while (i+depth) in seen:
                depth+=1
            
            res=max(res,depth)
        
        return res