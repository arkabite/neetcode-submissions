class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(l,r):
            rob1,rob2=0,0

            for i in range(l,r):
                temp=max(nums[i]+rob1,rob2)
                rob1=rob2
                rob2=temp
            return rob2
        

        robFirstHouse=helper(0,len(nums)-1)
        robLastHouse=helper(1,len(nums))
        
        return max(robFirstHouse,robLastHouse)
