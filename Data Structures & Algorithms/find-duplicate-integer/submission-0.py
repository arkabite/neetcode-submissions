class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
            if count[i]>1:
                return i