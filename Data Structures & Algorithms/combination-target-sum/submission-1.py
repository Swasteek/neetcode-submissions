class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(nums)
        def f(i,path,curr):
            if curr==target:
                res.append(path[:])
                return
            if curr>target or i>=n:
                return
            path.append(nums[i])
            f(i,path,curr+nums[i])
            path.pop()

            f(i+1,path,curr)
        f(0,[],0)
        return res