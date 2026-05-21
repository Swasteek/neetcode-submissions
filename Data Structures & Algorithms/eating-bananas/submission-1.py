class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(k):
            cnt=0
            for i in piles:
                cnt+=math.ceil(i/k)
            return cnt
        low,high=1,max(piles)
        while low<=high:
            mid=low+(high-low)//2
            cnt=f(mid)
            if cnt>h:
                low=mid+1
            else:
                high=mid-1
        return low