class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rli = [e for row in mat for e in row]
        return [rli[i*c: i*c+c] for i in range(r)] if r*c==len(rli) else mat