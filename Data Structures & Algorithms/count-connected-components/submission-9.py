class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[1]*n
        component=n
        def find(n):
            if parent[n]==n:
                return n
            
            parent[n]=find(parent[n])
            return parent[n]
        
        def union(n1,n2):
            boss1=find(n1)
            boss2=find(n2)

            if boss1==boss2:
                return 0

            if rank[boss2]>rank[boss1]:
                parent[boss1]=boss2
                rank[boss2]+=rank[boss1]
            else:
                parent[boss2]=boss1
                rank[boss1]+=rank[boss2]
            return 1
        
        res=n
        for u,v in edges:
            res-=union(u,v)
        
        return res
