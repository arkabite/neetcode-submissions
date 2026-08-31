class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D={i:[] for i in range(numCourses)}
        seen=set()
        for u,v in prerequisites:
            D[u].append(v)
        
        def dfs(val):
            if val in seen:
                return False

            if D[val]==[]:
                return True

            seen.add(val)
            for i in D[val]:
                if not dfs(i):
                    return False

            seen.remove(val)
            D[val]=[]

            return True
        
        for i in D:
            if not dfs(i):
                return False
        
        return True




