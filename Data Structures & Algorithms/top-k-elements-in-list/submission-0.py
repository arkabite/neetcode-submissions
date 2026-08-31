class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        asc=[i for i,v in sorted(count.items(),key=lambda item:item[1])]
        asc=asc[::-1]
        return asc[0:k]