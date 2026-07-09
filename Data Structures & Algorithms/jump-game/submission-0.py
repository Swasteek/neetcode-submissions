class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach=0
        n=len(nums)
        for i in range(n):
            if maxreach<i:
                break
            maxreach=max(maxreach,i+nums[i])
            if maxreach>=n-1:
                return True
        return False