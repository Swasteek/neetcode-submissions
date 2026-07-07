class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=[[False for i in range(cols)]for j in range(rows)]
        directions=[(0,-1),(-1,0),(1,0),(0,1)]
        def bfs(i,j):
            q=deque([(i,j)])
            visited[i][j]=True
            while q:
                a,b=q.popleft()
                for x,y in directions:
                    nx,ny=a+x,y+b
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]=="1" and not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny]=True
        cnt=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and not visited[i][j]:
                    bfs(i,j)
                    cnt+=1
        return cnt
                