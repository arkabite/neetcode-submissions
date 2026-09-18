class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[i for i,v in sorted(count.items(),key=lambda item:item[1],reverse=True)]
        return res[:k]