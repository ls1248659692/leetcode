class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m*n
        return min([e[0] for e in ops])*min([e[1] for e in ops])
        # ini = [[0 for c in  range(n)]for r in range(m)]
        
