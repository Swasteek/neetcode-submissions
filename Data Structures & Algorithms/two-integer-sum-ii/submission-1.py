class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        curr=nums[l]+nums[r]
        while curr!=target:
            if curr<target:
                l+=1
            else:
                r-=1
            curr=nums[l]+nums[r]
        return [l+1,r+1]