class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for i in strs:
            val=[0]*26
            for j in i:
                val[ord(j)-ord("a")]+=1
            res[tuple(val)].append(i)
        
        return list(res.values())