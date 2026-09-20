class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        seen=set()
        D={i:[] for i in range(n)}

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)

        def dfs(node,parent):
            if node in seen:
                return False
            
            seen.add(node)
            for i in D[node]:
                if parent==i:
                    continue
                
                if not dfs(i,node):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False
        
        return len(seen)==n