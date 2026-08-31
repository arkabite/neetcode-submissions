class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=l+1
        res=0
        while r<n:
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                res=max(res,profit)
            if prices[l]>prices[r]:
                l=r
            r+=1
        return res