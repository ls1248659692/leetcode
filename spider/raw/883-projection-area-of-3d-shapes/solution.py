class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        g,n,m = grid,len(grid),len(grid[0])
        rmx = sum(max(r) for r in g)
        cmx = sum(max([g[r][c] for r in range(n)]) for c in range(m))
        sm = sum(1 if g[r][c] else 0 for r in range(n)  for c in range(m))
        return rmx+cmx+sm