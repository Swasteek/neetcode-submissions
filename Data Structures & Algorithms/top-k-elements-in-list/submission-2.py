class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp={}
        for i in nums:
            mpp[i]=1+mpp.get(i,0)
        mh=[]
        for i,j in mpp.items():
            heapq.heappush(mh,(-j,i))
        res=[]
        for i in range(k):
            cnt,num=heapq.heappop(mh)
            res.append(num)
        return res