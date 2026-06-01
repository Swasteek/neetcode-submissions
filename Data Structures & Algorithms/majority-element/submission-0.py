class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        ele=float('inf')
        for i in nums:
            if i==ele:
                cnt+=1
            else: 
                cnt-=1
            if cnt<0:
                cnt=1
                ele=i
        return ele