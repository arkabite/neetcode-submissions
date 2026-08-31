class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        component=n

        def find(node):

            if parent[node]==node:
                return node
            
            parent[node]=find(parent[node])
            return parent[node]
        
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
