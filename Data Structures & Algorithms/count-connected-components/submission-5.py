class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[1]*n

        def find(n):
            res=n

            while res!=parent[res]:
                parent[res]=parent[parent[res]]
                res=parent[res]
            
            return res
        
        def union(n1,n2):
            boss1=find(n1)
            boss2=find(n2)

            if boss1==boss2:
                return 0
            
            if rank[boss2]>rank[boss1]:
                parent[boss1]=boss2
                rank[boss2]+=boss1
            else:
                parent[boss2]=boss1
                rank[boss1]+=boss2
            return 1
        
        res=n
        for u,v in edges:
            res-=union(u,v)
        
        return res
            