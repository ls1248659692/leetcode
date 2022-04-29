class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            matrix[i],  matrix[-1-i] = matrix[-1-i], matrix[i]
        for j in range(n):
            for k in range(j+1, n):
                matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]