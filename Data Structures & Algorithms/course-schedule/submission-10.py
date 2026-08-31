class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D={i:[] for i in range(numCourses)}
        seen=set()
        for u,v in prerequisites:
            D[u].append(v)
        
    
        def dfs(i):
            if i==numCourses:
                return True

            if i in seen:
                return False
            
            if D[i]==[]:
                return True

            seen.add(i)
            for j in D[i]:
                if not dfs(j):
                    return False
            seen.remove(i)
            D[i]=[]
            return True
        
        for i in D:
            if not dfs(i):
                return False
        
        return True
