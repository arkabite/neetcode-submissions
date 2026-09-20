class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D={i:[] for i in range(numCourses)}
        visit=set()
        for u,v in prerequisites:
            D[u].append(v)
        
        def dfs(crs):
            if crs in visit:
                return False

            if D[crs]==[]:
                return True
            
            visit.add(crs)
            for i in D[crs]:
                if not dfs(i):
                    return False
            
            visit.remove(crs)
            D[crs]=[]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
