class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, k):
            # matched full word
            if k == len(word):
                return True
            
            # boundary + mismatch
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[k]:
                return False
            
            # mark visited
            temp = board[i][j]
            board[i][j] = "#"
            
            # explore 4 directions
            found = (
                dfs(i+1, j, k+1) or
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1)
            )
            
            # backtrack
            board[i][j] = temp
            
            return found
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False