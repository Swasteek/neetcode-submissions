class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+2)
        # def f(ind):
        #     if ind>=n:
        #         return 0
        #     if dp[ind]!=-1:
        #         return dp[ind]
        #     rob=nums[ind]+f(ind+2)
        #     notRob=f(ind+1)
        #     dp[ind]=max(rob,notRob)
        #     return dp[ind]
        
        for i in range(n-1,-1,-1):
            dp[i]=max(dp[i+1],nums[i]+dp[i+2])
        
        return dp[0]