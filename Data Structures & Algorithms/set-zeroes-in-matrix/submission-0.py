class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        s=[]
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    s.append([i,j])
        for i,j in s:
            for x in range(cols):
                matrix[i][x]=0
            for x in range(rows):
                matrix[x][j]=0
        