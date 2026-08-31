class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=defaultdict(int)
        n=len(s)
        l=0
        r=0
        res=0
        while r<n:
            count[s[r]]+=1
            while count[s[r]]>1:
                count[s[l]]-=1
                l+=1
            res=max(res,((r-l)+1))
            r+=1
        return res