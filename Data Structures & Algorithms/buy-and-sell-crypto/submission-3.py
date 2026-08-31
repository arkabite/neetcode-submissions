class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=l+1
        res=0
        while r<n:
            if prices[l]>prices[r]:
                l=r
                continue
            val=prices[r]-prices[l]
            res=max(res,val)
            r+=1
        return res
