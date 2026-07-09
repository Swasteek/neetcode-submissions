class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref=suff=1
        maxi=float('-inf')
        n=len(nums)
        for i in range(n):
            pref*=nums[i]
            suff*=nums[n-i-1]
            maxi=max(pref,suff,maxi)
            if pref==0:
                pref=1
            if suff==0:
                suff=1
        return maxi
