class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo={}
        minLen=0
        res=""
        def dfs(l,r):
            if l>=r:
                return True
            if (l,r) in memo:
                return memo[(l,r)]
            
            memo[(l,r)]=(s[l]==s[r]) and dfs(l+1,r-1)
            return memo[(l,r)]
        
        for l in range(len(s)):
            for r in range(l,len(s)):
                if dfs(l,r):
                    if ((r-l)+1)>minLen:
                        minLen=((r-l)+1)
                        res=s[l:r+1]
        
        return res

        
