class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp={}
        for i in nums:
            mpp[i]=1+mpp.get(i,0)
        mh=[]
        for val,cnt in mpp.items():
            heapq.heappush(mh,(-cnt,val))
        res=[]
        for i in range(k):
            cnt,val=heapq.heappop(mh)
            res.append(val)
        return res