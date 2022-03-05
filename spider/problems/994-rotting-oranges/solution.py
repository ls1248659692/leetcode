class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        g,m,n = grid,len(grid),len(grid[0])
        bad=[(i,j) for i in range(m) for j in range(n) if g[i][j]==2]
        aset,tset,sec=set(bad),set(bad),0
        while aset:
            _aset,aset=set(aset),set()
            for i,j in _aset:
                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    ii,jj=i+x,j+y
                    if 0<=ii<m and 0<=jj<n and g[ii][jj]==1 and (ii,jj) not in tset:
                        aset.add((ii,jj))
            if aset: sec+=1
            for pt in aset:tset.add(pt)
        return -1 if [(i,j) for i in range(m) for j in range(n) if g[i][j]==1 and (i,j) not in tset] else sec