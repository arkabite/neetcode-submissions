class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        D={i:[] for i in range(n)}
        seen=set()
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        
        def dfs(i,parent):
            if i in seen:
                return False
            
            seen.add(i)
            for j in D[i]:
                if j==parent:
                    continue
                
                if not dfs(j,i):
                    return False
            seen.remove(i)
            return True
        
        for i in D:
            if not dfs(i,-1):
                return False
        
        print(D)
        
        return True
