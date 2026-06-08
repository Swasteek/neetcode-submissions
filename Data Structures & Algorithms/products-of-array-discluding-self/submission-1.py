class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc=0
        mul=1
        n=len(nums)
        res=[0]*n
        zind=-1
        for i in range(n):
            if nums[i]:
                mul*=nums[i]
            else:
                zc+=1
                zind=i
        if zc>=2:
            return res
        elif zc==1:
            res[zind]=mul
            return res
        for i in range(n):
            res[i]=mul//nums[i]
        return res


        