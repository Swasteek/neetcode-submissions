class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pac=[[False]*cols for i in range(rows)]
        alt=[[False]*cols for i in range(rows)]
        directions=[(-1,0),(0,-1),(0,1),(1,0)]
        def bfs(source,ocean):
            q = deque()

            for i, j in source:
                if not ocean[i][j]:
                    ocean[i][j] = True
                    q.append((i, j))
            while q:
                i,j=q.popleft()
                for x,y in directions:
                    nx,ny=i+x,j+y
                    if 0<=nx<rows and 0<=ny<cols and not ocean[nx][ny] and heights[nx][ny]>=heights[i][j]:
                        q.append((nx,ny))
                        ocean[nx][ny]=True
        p,a=[],[]
        for i in range(cols):
            p.append((0,i))
            a.append((rows-1,i))
        for i in range(rows):
            p.append((i,0))
            a.append((i,cols-1))
        
        bfs(a,alt)
        bfs(p,pac)
        res=[]
        for i in range(rows):
            for j in range(cols):
                if pac[i][j] and alt[i][j]:
                    res.append([i,j])
        return res
        
