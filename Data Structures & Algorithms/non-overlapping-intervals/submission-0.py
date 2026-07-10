class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x:x[1])
        n=len(nums)
        cnt=0
        lnd=nums[0][1]
        for i in range(1,n):
            if nums[i][0]>=lnd:
                cnt+=1
                lnd=nums[i][1]
        return n-cnt-1
        