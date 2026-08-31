class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        res=0
        l=0
        r=1
        while r<n:
            profit=prices[r]-prices[l]
            res=max(res,profit)
            if prices[r]<prices[l]:
                l=r
            r+=1
        
        return res