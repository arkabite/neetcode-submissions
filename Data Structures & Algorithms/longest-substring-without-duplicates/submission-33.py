class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        n=len(s)
        l=0
        count={}
        for r in range(n):
            count[s[r]]=count.get(s[r],0)+1

            while count[s[r]]>1:
                count[s[l]]=count.get(s[l],0)-1
                l+=1
            
            res=max(res,(r-l)+1)

        return res