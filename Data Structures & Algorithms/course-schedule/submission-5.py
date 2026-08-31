class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D={i:[] for i in range(numCourses)}
        seen=set()
        for u,v in prerequisites:
            D[u].append(v)
        

        def dfs(node):
            if node in seen:
                return False
            if D[node]==[]:
                return True
            
            seen.add(node)
            for i in D[node]:
                if not dfs(i):
                    return False
            seen.remove(node)
            D[node]=[]
            return True
        
        for i in D:
            if not dfs(i):
                return False

        return True