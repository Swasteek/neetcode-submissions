class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        def f(ind):
            if ind>=n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            ans=min(f(ind+1),f(ind+2))+cost[ind]
            dp[ind]=ans
            return ans
        return min(f(0),f(1))
        