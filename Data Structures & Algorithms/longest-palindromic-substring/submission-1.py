class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo={}
        res=""

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
                    if ((r-l)+1)>len(res):
                        res=s[l:r+1]
        
        return res