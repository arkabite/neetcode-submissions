class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,v in enumerate(nums):
            rem=target-v
            if rem in seen:
                return [seen[rem],i]
            seen[v]=i