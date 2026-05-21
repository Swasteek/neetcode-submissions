from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        # Step 1: push all gates
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        
        # Step 2: BFS
        while q:
            x, y = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    # only update empty rooms
                    if grid[nx][ny] == 2147483647:
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx, ny))