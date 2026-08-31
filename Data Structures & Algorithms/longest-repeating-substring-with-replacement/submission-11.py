class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        if n==0:
            return 0
        res=1
        l=0
        r=0
        maxfreq=0
        count=defaultdict(int)
        while r<n:
            count[s[r]]+=1
            maxfreq=max(maxfreq,count[s[r]])
            while ((r-l)+1)-maxfreq>k:
                count[s[l]]-=1
                l+=1
            res=max(res,(r-l)+1)
            r+=1
        return res