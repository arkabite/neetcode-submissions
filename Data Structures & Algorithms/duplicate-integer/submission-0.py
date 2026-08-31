class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett=set(nums)
        if len(sett)<len(nums):
            return True
        else:
            return False