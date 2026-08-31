class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D=defaultdict(list)
        seen=set()
        for u,v in prerequisites:
            D[u].append(v)
        
        def dfs(crs):
            if crs in seen:
                return False
            if not D[crs]:
                return True

            seen.add(crs)
            for i in D[crs]:
                if not dfs(i):
                    return False

            seen.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
