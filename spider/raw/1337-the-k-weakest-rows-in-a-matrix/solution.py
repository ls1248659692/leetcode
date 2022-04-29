class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li =[(sum(mat[i]),i) for i in range(len(mat))]
        return [e[1] for e in sorted(li,key=lambda x: x[0]*1000 + x[1])][:k]