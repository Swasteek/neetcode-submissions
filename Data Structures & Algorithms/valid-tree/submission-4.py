class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par=[i for i in range(n)]
        cnt=[n]
        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                par[py]=px
                cnt[0]-=1
                return True
            else:
                return False
        for i,j in edges:
            if not union(i,j):
                return False
        return cnt[0]==1
