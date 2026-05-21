class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        path=[]
        n=len(nums)
        nums.sort()
        def backtrack(i):
            if i==n:
                ans.add(tuple(path))
                return
            backtrack(i+1)
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
        backtrack(0)
        return [list(x) for x in ans]