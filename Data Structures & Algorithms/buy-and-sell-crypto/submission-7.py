class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=l+1
        res=0
        while r<n:
            profit=prices[r]-prices[l]
            if prices[l]>prices[r]:
                l=r
            res=max(res,profit)
            r+=1
        return res