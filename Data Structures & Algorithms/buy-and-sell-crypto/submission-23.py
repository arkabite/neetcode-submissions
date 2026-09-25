class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        res=0
        for r in range(n):
            profit=prices[r]-prices[l]
            res=max(res,profit)
            if prices[r]<prices[l]:
                l=r
        
        return res