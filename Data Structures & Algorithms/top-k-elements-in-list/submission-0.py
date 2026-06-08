import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp={}
        for i in nums:
            mpp[i]=1+mpp.get(i,0)
        minh=[]
        for key,val in mpp.items():
            heapq.heappush(minh,(-val,key))
        
        ans=[]
        for i in range(k):
            val,node=heapq.heappop(minh)

            ans.append(node)
        return ans