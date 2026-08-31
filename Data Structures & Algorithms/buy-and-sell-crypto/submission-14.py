class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        n=len(prices)
        l=0
        r=l+1
        while r<n:
            profit=prices[r]-prices[l]
            res=max(res,profit)
            if prices[r]<prices[l]:
                l=r
            r+=1
        return res