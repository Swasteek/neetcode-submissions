class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        visited=[[False for i in range(cols)] for j in range(rows)]
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        def bfs(i,j):
            if visited[i][j]:
                return 
            visited[i][j]=True
            q=deque([(i,j)])
            while q:
                x,y=q.popleft()
                for a,b in directions:
                    nx,ny=x+a,y+b
                    if 0<=nx<rows and 0<=ny<cols and board[nx][ny]=='O' and not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny]=True

        for i in range(rows):
            if board[i][0]=='O':
                bfs(i,0)
            if board[i][cols-1]=='O':
                bfs(i,cols-1)
        for i in range(cols):
            if board[0][i]=='O':
                bfs(0,i)
            if board[rows-1][i]=='O':
                bfs(rows-1,i)

        for i in range(1,rows):
            for j in range(1,cols):
                if board[i][j]=='O' and not visited[i][j]:
                    board[i][j]='X'