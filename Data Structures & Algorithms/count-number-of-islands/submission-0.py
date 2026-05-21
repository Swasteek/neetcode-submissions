class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=[[False for i in range(cols)] for j in range(rows)]
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        def dfs(i,j):
            q=deque([(i,j)])
            while q:
                x,y=q.popleft()
                for a,b in directions:
                    nx,ny=x+a,y+b
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]=="1" and  not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny]=True
        islands=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and not visited[i][j]:
                    visited[i][j]=True
                    dfs(i,j)
                    islands+=1
        return islands   

        