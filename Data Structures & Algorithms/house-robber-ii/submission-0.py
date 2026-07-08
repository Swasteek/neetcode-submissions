class Solution:
    def rob1(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+2)
        for i in range(n-1,-1,-1):
            dp[i]=max(dp[i+1],dp[i+2]+nums[i])
        return dp[0]
        
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        return max(self.rob1(nums[:-1]),self.rob1(nums[1:]))
        