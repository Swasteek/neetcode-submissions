class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxi=0
        for i in s:
            if i-1 not in s:
                x=i
                cnt=1
                while x+1 in s:
                    x+=1
                    cnt+=1
                maxi=max(maxi,cnt)
        return maxi