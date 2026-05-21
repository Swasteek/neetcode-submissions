class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)

        def backtrack(ind):
            if ind==n:
                ans.append(nums[:])
                return
            for i in range(ind,n):
                nums[ind],nums[i]=nums[i],nums[ind]
                backtrack(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]        
        backtrack(0)
        return ans