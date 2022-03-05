class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def max_link(r,c,hset):
            h= g[r][c]
            for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:      
                rr,cc,h1= r+i,c+j,h+1          
                if 0<=rr<m and 0<=cc<n and  h1<g[rr][cc]:
                    g[rr][cc]=h1
                    hset.add((rr,cc))

        g,m,n= grid,len(grid),len(grid[0])
        if sum(sum(r) for r in g) in [0,n*m]:return -1
        m_n= m*n
        g = [ [0 if g[i][j]==1 else m_n for j in range(n)] for i in range(m)]
        hset = [(i,j) for i in range(m) for j in range(n) if g[i][j]==0]
        for h in range(0,m_n+1):
            _hset,hset=set(hset),set()
            for r,c in _hset:
                max_link(r,c,hset)
        return max(max(r) for r in g)