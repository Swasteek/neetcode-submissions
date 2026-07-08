class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            res.append(self.myc(i))
        return res
    def myc(self,n):
        cnt=0
        while(n):
            cnt+=n&1
            n=n>>1
        return cnt
        