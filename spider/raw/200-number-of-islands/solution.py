class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def max_link(img,sr,sc):
            iset,isetb =set([(sr,sc)]) ,set()
            while iset != isetb:
                isetb=set(iset)
                for r,c in isetb:
                    for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if 0<=r+i<len(img) and 0<=c+j<len(img[0]) and img[r+i][c+j] ==img[sr][sc]: iset.add((r+i,c+j))     
            return iset

        tot1 = sum(el=='1' for row in grid for el in row)
        inum ,tset = 0,set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1' and (r,c) not in tset:
                    inum +=1
                    tset =tset.union( max_link(grid,r,c))
        return inum