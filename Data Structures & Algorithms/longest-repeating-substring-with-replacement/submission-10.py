class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        count=defaultdict(int)
        l=0
        maxfreq=0
        res=0
        for r in range(n):
            count[s[r]]+=1
            maxfreq=max(maxfreq,count[s[r]])
            while ((r-l)+1)-maxfreq>k:
                count[s[l]]-=1
                l+=1
            res=max(res,(r-l)+1)
        
        return res
