class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def max_link(g,sr,sc):
            iset,isetb =set([(sr,sc)]) ,set()
            while iset != isetb:
                isetb=set(iset)
                for r,c in isetb:
                    for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if 0<=r+i<n and 0<=c+j<m and g[r+i][c+j] ==g[sr][sc]: iset.add((r+i,c+j))     
            return iset

        g,n,m=grid,len(grid),len(grid[0])
        for r in g:print(r)
        inum ,tset,islands = 0,set(),[]
        
        for r in range(n):
            for c in range(m):
                if g[r][c]==1 and (r,c) not in tset:
                    inum +=1
                    iset = max_link(g,r,c)
                    tset =tset.union(iset )
                    islands.append(iset)
        cnt=sum(sum([1 for x,y in isl if x in (0,n-1) or y in (0,m-1)])==0 for isl in islands) if islands else 0
        return sum(len(isl) for isl in islands if sum([1 for x,y in isl if x in (0,n-1) or y in (0,m-1)])==0) if islands else 0       