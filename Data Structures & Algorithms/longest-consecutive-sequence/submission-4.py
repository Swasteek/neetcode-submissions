class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=set(nums)
        maxi=1
        for i in s:
            if i-1 not in s:
                cnt=1
                x=i
                while x+1 in s:
                    cnt+=1
                    x+=1
                maxi=max(maxi,cnt)
        return maxi