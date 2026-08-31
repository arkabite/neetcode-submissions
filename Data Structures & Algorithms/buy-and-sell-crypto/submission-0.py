class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        res=0
        for i in range(n):
            l=i
            r=n-1
            while l<r:
                val=prices[r]-prices[l]
                res=max(res,val)
                r-=1
        return res


