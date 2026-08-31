class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*n

        for i in range(n):
            cur=temperatures[i]

            while stack and temperatures[stack[-1]]<cur:
                val=stack.pop()
                res[val]=i-val

            stack.append(i)
        
        return res
