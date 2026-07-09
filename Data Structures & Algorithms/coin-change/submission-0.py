class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1 for i in range(amount+1)]for j in range(n+1)]

        def f(i,rem):
            if rem==0:
                return 0
            if i>=n or rem<0:
                return int(1e9)
            if dp[i][rem]!=-1:
                return dp[i][rem]
            take=1+f(i,rem-coins[i])
            skip=f(i+1,rem)
            dp[i][rem]=min(take,skip)
            return dp[i][rem]
        ans=f(0,amount)
        return -1 if ans>=int(1e9) else ans