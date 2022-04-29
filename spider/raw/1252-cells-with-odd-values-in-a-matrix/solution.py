class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for a in range(n)] for b in range(m)]
        for i in indices:
            for x in range(n):
                matrix[i[0]][x] = matrix[i[0]][x] + 1
            for y in range(m):
                matrix[y][i[1]] = matrix[y][i[1]] + 1
        count = 0
        for row in matrix:
            for ele in row:
                if ele % 2 == 1:
                    count = count + 1
        return count