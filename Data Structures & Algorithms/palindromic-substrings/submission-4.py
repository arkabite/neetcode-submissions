class Solution:
    def countSubstrings(self, s: str) -> int:
        memo={}
        res=0
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
                    res+=1
        
        return res