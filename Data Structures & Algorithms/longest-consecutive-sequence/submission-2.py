class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        sett=list(sett)
        res=0
        stack=[]
        finalRes=0
        sett.sort()
        for i in range(len(sett)):
            while stack and abs(sett[i]-stack[-1])!=1:
                stack.pop()
                res=0
            else:
                stack.append(sett[i])
                res+=1
                finalRes=max(finalRes,res)
        return finalRes
        
