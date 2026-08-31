class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        D={i:[] for i in range(n)}
        seen=set()
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        
        res=0
        
        def dfs(i):
            seen.add(i)
            for j in D[i]:
                if j not in seen:
                    dfs(j)
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        
        return res

            
        
