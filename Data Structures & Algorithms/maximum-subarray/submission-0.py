class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi=0
        maxi=float('-inf')
        for i in nums:
            sumi+=i
            maxi=max(maxi,sumi)
            if sumi<0:
                sumi=0
            
        return maxi