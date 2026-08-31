class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols=len(matrix),len(matrix[0])
        row=set()
        col=set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in row or c in col:
                    matrix[r][c]=0
        
        