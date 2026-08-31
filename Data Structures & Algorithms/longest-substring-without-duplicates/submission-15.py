class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        if n==1:
            return 1
        l=0
        r=l+1
        sett=set(s[l])
        res=0
        while r<n: 
            if s[r] in sett:
                sett.remove(s[l])
                l+=1
            else:
                res=max(res,(r-l)+1)
                sett.add(s[r])
                r+=1
        return res
