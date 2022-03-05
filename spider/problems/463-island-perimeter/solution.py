class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def v1(grid):
            count = 0 
            ans = [ [] for i in range(len(grid))]
            marginx = len(grid)
            marginy = len(grid[0])
            for i in range(len(grid)):
                grid[i].insert(0,0)
                grid[i].append(0)
            grid.append([0] * (len(grid[0])))
            grid.insert(0,[0] * (len(grid[0])))
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == 1:
                        if grid[x][y+1] == 0:
                            count = count+ 1
                        if grid[x][y-1] == 0:
                            count = count+ 1
                        if grid[x+1][y] == 0:
                            count = count+ 1
                        if grid[x-1][y] == 0:
                            count = count+ 1
                        print(x,y,count)

            return count

        def v0(grid):
            g,n,m = grid, len(grid),len(grid[0])
            #g = [[0]*(m+2)] +  [[0]+r+[0] for r in grid] + [[0]*(m+2)]
            v = lambda i,j: g[i][j] if 0<=i<n and 0<=j<m else 0
            for r in g:print(r)
            perim=0
            for i in range(0,n):
                for j in range(0,m):
                    if g[i][j]:
                        #perim +=4
                        #perim -= g[i-1][j] + g[i][j-1]+g[i][j+1] + g[i+1][j]
                        for x,y in [(-1,0),(0,-1),(1,0),(0,1)]: perim += 1 if v(i+x,j+y)==0 else 0
                        #perim -= g[i-1][j] + g[i][j-1]+g[i][j+1] + g[i+1][j]
            return perim
        return v0(grid)