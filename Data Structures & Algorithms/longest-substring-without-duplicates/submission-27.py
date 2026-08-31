class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        count=defaultdict(int)
        l=0
        res=0
        for r in range(n):  
            count[s[r]]+=1

            while count[s[r]]>1:
                count[s[l]]-=1
                l+=1
            
            res=max(res,((r-l)+1))
        
        return res