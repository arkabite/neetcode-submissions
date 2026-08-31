class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        rows=m
        cols=n
        def dfs(r,c):
            if (r,c)==(rows-1,cols-1):
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            if r>=rows or c>=cols or r<0 or c<0:
                return 0
            
            val= dfs(r+1,c) + dfs(r,c+1)
            memo[(r,c)]=val
            return memo[(r,c)]
        
        return dfs(0,0)