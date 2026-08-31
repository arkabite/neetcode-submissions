class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
            
        D={i:[] for i in range(n)}
        seen=set()

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        
        def dfs(node,parent):
            if node in seen:
                return False
            
            seen.add(node)
            for i in D[node]:
                if i==parent:
                    continue
                
                if not dfs(i,node):
                    return False

            return True

        dfs(0,-1)
        return len(seen)==n