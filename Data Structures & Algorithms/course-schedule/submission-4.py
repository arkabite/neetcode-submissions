class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D={i:[] for i in range(numCourses)}

        for u,v in prerequisites:
            D[u].append(v)
        
        seen=set()
        def dfs(crs):
            if crs in seen:
                return False
            if D[crs]==[]:
                return True
            
            seen.add(crs)
            for i in D[crs]:
                if not dfs(i):
                    return False
            seen.remove(crs)
            D[crs]=[]

            return True
        
        for i in D:
            if not dfs(i):
                return False
        return True