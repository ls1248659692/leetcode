class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g,n,m = grid,len(grid),len(grid[0])
        zskip = lambda i,j,x: 99999 if not 0<=i<n or not 0<=j<m else x
        f=[[g[0][0]]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:continue
                f[i][j]= min(zskip(i,j-1,f[i][j-1]),zskip(i-1,j,f[i-1][j]))+g[i][j]
        return f[-1][-1]        