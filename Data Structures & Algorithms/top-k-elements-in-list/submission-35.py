class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for i in range(len(nums)+1)]
        res=[]
        for i,v in count.items():
            freq[v].append(i)
        
        for j in range(len(freq)-1,-1,-1):
            for val in freq[j]:
                res.append(val)
                if len(res)==k:
                    return res
