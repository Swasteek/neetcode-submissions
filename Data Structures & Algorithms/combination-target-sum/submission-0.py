class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        n=len(nums)
        def f(i,target):
            
            if target==0:
                ans.append(path[:])
                return
            if i >= n or target < 0:
                return
            
            f(i+1,target)
            path.append(nums[i])
            f(i,target-nums[i])
            path.pop()
        f(0,target)
        return ans
        