class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        D={i:[] for i in range(n)}
        seen=set()

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        
        print(D)
        def dfs(i,parent):
            if i in seen:
                return False
            
            seen.add(i)
            print(seen)
            for val in D[i]:
                if val==parent:
                    continue
                
                if not dfs(val,i):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False
        
        return len(seen)==n
