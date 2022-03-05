class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cnt,g,m,n,gt = 0,grid,len(grid),len(grid[0]),list(zip(*grid))
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    if g[i].count(1) + gt[j].count(1) > 2:
                        cnt += 1
        return cnt