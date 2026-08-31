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
        while r<n:
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            res=max(res,len(sett))
            r+=1
        return res