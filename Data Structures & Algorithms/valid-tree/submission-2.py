class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par=[i for i in range(n)]
        cnt=[n]
        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(x,y):
            parx,pary=find(x),find(y)
            if parx==pary:
                return False
            
            par[parx]=pary
            cnt[0]-=1
            return True
        
        for u,v in edges:
            if not union(u,v):
                return False
        return True if cnt[0]==1 else False