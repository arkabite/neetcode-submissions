class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols=m,n
        memo={}
        def dfs(r,c):
            if (r,c)==(rows-1,cols-1):
                return 1
            
            if r<0 or c<0 or r>=rows or c>=cols:
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            val=dfs(r+1,c) + dfs(r,c+1)
            memo[(r,c)]=val
            return memo[(r,c)]
        
        return dfs(0,0)