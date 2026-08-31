class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        n=len(s)
        if n==0:
            return 0
        res=1
        l=0
        r=l+1
        sett.add(s[l])
        while r<n and l<=r:
            if s[r] in sett:
                sett.remove(s[l])
                l+=1
            else:
                sett.add(s[r])
                r+=1
            res=max(len(sett),res)
        return res