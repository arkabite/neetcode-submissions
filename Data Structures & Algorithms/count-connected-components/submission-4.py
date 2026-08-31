class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        component=n
        def find(n):

            if parent[n]==n:
                return n
            
            parent[n]=find(parent[n])
            return parent[n]

        def union(u,v):
            nonlocal component
            boss1=find(u)
            boss2=find(v)
            if boss1!=boss2:
                parent[boss1]=boss2
                component-=1
        
        for u,v in edges:
            union(u,v)
        
        return component