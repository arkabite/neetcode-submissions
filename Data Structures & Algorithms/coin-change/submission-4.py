class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(rem):
            if rem==0:
                return 0
            if rem<0:
                return -1
            if rem in memo:
                return memo[rem]
            
            minCoin=float("inf")

            for i in coins:
                res=dfs(rem-i)

                if res!=-1:
                    minCoin=min(minCoin,res+1)
            memo[rem]=minCoin if minCoin!=float("inf") else -1
            return memo[rem]

        return dfs(amount)
            