class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        long=0
        for i in s:
            if i-1 not in s:
                x=i
                cnt=0
                while x in s:
                    cnt+=1
                    x+=1
                long=max(long,cnt)
        return long