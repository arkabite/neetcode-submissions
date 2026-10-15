class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[] 
        sol=[]
        n=len(nums)
        def dfs(i,val):
            if val==target:
                res.append(sol[:])
                return 
            if i>=n or val>target:
                return 

            sol.append(nums[i])
            dfs(i,val+nums[i])
            sol.remove(nums[i])
            dfs(i+1,val)
        
        dfs(0,0)
        return res