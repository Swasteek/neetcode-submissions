class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        ans = []
        path = []
        n = len(nums)
        
        def f(i, target):
            
            if target == 0:
                ans.append(path[:])
                return
            
            for x in range(i, n):
                
                # skip duplicates
                if x > i and nums[x] == nums[x-1]:
                    continue
                
                # pruning
                if nums[x] > target:
                    break
                
                path.append(nums[x])
                f(x + 1, target - nums[x])
                path.pop()
        
        f(0, target)
        return ans