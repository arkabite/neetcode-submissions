class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        memo={}

        def dfs(i,j):
            if i>=j:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)]=(s[i]==s[j]) and dfs(i+1,j-1)
            return memo[(i,j)]
        
        for l in range(len(s)):
            for r in range(l,len(s)):
                if dfs(l,r):
                    res+=1

        return res