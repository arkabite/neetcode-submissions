class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        D={i:[] for i in range(n)}

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        print(D)
        seen=set()
        res=0
        def dfs(node):
            seen.add(node)
            for i in D[node]:
                if i not in seen:
                    dfs(i)
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        
        return res