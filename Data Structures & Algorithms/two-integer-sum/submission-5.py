class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i,v in enumerate(nums):
            val=target-v
            if val in seen:
                return [seen[val],i]
            else:
                seen[v]=i