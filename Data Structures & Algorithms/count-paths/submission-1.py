class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        rows=m
        cols=n
        res=0
        def dfs(r,c):
            nonlocal res
            if r>=rows or c>=cols:
                return 0
            if (r,c)==(rows-1,cols-1):
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            
            val=dfs(r+1,c)+dfs(r,c+1)
            memo[(r,c)]=val
            return memo[(r,c)]
        
        return dfs(0,0)