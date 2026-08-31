class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def helper(houses):
            rob1,rob2=0,0

            for i in houses:
                temp=max(i+rob1,rob2)
                rob1=rob2
                rob2=temp
            
            return rob2
        
        return max(nums[0],helper(nums[1:]),helper(nums[:len(nums)-1]))
            