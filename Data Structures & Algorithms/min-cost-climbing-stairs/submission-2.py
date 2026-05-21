class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n+2)
        def f(ind):
            if ind>=n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            ans=min(f(ind+1),f(ind+2))+cost[ind]
            dp[ind]=ans
            return ans
        for ind in range(n-1,-1,-1):
            ans=min(dp[ind+1],dp[ind+2])+cost[ind]
            dp[ind]=ans
        return min(dp[0],dp[1])
        