class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord("a")]+=1
            seen[tuple(count)].append(i)
        return list(seen.values()) if seen else None
        