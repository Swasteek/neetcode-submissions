from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            ind=bisect_left(ans,i)
            if ind==len(ans):
                ans.append(i)
            else:
                ans[ind]=i
        return len(ans)
