class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        D={i:[] for i in range(n)}
        res=0        
        seen=set()

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)

        def dfs(i):
            seen.add(i)
            for val in D[i]:
                if val not in seen:
                    dfs(val)
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        
        return res