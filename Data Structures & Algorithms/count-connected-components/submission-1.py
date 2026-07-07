class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par=[i for i in range(n)]
        cnt=[n]
        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(x,y):
            parx,pary=find(x),find(y)
            if parx==pary:
                return 
            
            par[parx]=pary
            cnt[0]-=1
        
        for u,v in edges:
            union(u,v)
        
        return cnt[0]

        