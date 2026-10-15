class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D={i:[] for i in range(numCourses)}
        visit=set()
        for u,v in prerequisites:
            D[u].append(v)
        
        def dfs(i):
            if i in visit:
                return False
            
            if D[i]==[]:
                return True

            visit.add(i)
            for val in D[i]:
                if not dfs(val):
                    return False
            visit.remove(i)
            D[i]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True