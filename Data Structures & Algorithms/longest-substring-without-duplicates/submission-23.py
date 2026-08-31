class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        res=0
        l=0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            r+=1
            res=max(res,len(sett))
        
        return res


