class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_l = [min(x) for x in matrix]
        max_l = []
        res = []
        for j in range(len(matrix[0])):
            row = []
            for i in matrix:
                row.append(i[j])
            max_l.append(max(row))
        for val in min_l:
            if val in max_l:
                res.append(val)
        return res
