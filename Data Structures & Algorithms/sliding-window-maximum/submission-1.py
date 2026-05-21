from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()  # stores indices
        res = []
        
        for i in range(len(nums)):
            
            # 1. Remove out-of-window elements
            while q and q[0] <= i - k:
                q.popleft()
            
            # 2. Maintain decreasing order
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            # 3. Add current index
            q.append(i)
            
            # 4. Record answer
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res