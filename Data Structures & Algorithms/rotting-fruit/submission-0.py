class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        fresh=0
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        time=0
        while q and fresh > 0:
            for _ in range(len(q)):
                i,j=q.popleft()
                for x,y in directions:
                    nx,ny=i+x,j+y
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        fresh-=1
                        q.append((nx,ny))
            time+=1
        return time if fresh==0 else -1
        