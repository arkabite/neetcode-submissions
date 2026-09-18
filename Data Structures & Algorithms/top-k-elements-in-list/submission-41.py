class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        freq=[[] for i in range(len(nums)+1)]

        for i,v in count.items():
            freq[v].append(i)
        
        for i in range(len(freq)-1,-1,-1):
            for val in freq[i]:
                res.append(val)
                if len(res)==k:
                    return res