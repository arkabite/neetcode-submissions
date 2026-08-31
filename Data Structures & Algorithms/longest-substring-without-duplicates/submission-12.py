class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        n=len(s)
        if n==0:
            return 0
        l=0
        r=l+1
        sett.add(s[l])
        res=1
        while r<n and l<=r:
            if s[r] in sett:
                sett.remove(s[l])
                l+=1
            else:
                sett.add(s[r])
                res=max(res,len(sett))
                r+=1
        return res