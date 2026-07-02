class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,n-1
            while j<k:
                sumi=nums[i]+nums[j]+nums[k]
                if sumi==0:
                    s.add(tuple([nums[i],nums[j],nums[k]]))
                    k-=1
                    j+=1
                elif sumi>0:
                    k-=1
                else:
                    j+=1
        return [list(x) for x in s]