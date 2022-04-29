class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def max_link(g,sr,sc):
            iset,isetb =set([(sr,sc)]) ,set()
            while iset != isetb:
                isetb=set(iset)
                for r,c in isetb:
                    for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if 0<=r+i<len(g) and 0<=c+j<len(g[0]) and g[r+i][c+j] ==g[sr][sc]: iset.add((r+i,c+j))     
            return iset

        inum ,tset,islands = 0,set(),[]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1 and (r,c) not in tset:
                    inum +=1
                    iset = max_link(grid,r,c)
                    tset =tset.union(iset )
                    islands.append(iset)
        return max(len(isl) for isl in islands) if islands else 0        