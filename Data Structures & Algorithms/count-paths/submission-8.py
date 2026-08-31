class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        rows=m
        cols=n
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 0
            
            if (r,c)==(rows-1,cols-1):
                return 1
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)]=dfs(r+1,c)+dfs(r,c+1)
            return memo[(r,c)]

        return dfs(0,0)
        