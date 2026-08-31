class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}

        def dfs(rem):
            if rem<0:
                return -1
            if rem==0:
                return 0

            if rem in memo:
                return memo[rem]

            minCoinCount=float("inf")

            for i in coins:
                res=dfs(rem-i)

                if res!=-1:
                    minCoinCount=min(minCoinCount,res+1)
            memo[rem]=minCoinCount
            return memo[rem] if minCoinCount!=float("inf") else -1
        
        return dfs(amount)