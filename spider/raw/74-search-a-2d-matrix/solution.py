class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        g,m,n= matrix,len(matrix),len(matrix[0])
        return target in [g[i][j]  for i in range(m) for j in range(n)]