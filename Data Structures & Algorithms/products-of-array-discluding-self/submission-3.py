class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        prod=1
        cnt=0
        for i in range(n):
            if nums[i]:
                prod*=nums[i]
            else:
                cnt+=1
                ind=i
        if cnt>=2:
            return res
        if cnt==1:
            res[ind]=prod
            return res
        for i in range(n):
            res[i]=prod//nums[i]
        return res