class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,zero=1,0
        for i in nums:
            if i:
                prod*=i
            else:
                zero+=1
        res=[0]*len(nums)
        if zero>=2:
            return res
        for i in range(len(nums)):
            if nums[i]==0:
                res[i]=prod
            elif zero<1:
                res[i]=prod//nums[i]
        return res