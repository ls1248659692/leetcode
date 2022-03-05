# [Island Perimeter][title]

## Description

给定一个 `row x col` 的二维网格地图 `grid` ，其中：`grid[i][j] = 1` 表示陆地， `grid[i][j] = 0`
表示水域。

网格中的格子 **水平和垂直**
方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
。计算这个岛屿的周长。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/10/12/island.png)
            **输入：** grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]    **输出：** 16    **解释：** 它的周长是上面图片中的 16 个黄色的边

**示例 2：**
            **输入：** grid = [[1]]    **输出：** 4    

**示例 3：**
            **输入：** grid = [[1,0]]    **输出：** 4    

**提示：**

  * `row == grid.length`
  * `col == grid[i].length`
  * `1 <= row, col <= 100`
  * `grid[i][j]` 为 `0` 或 `1`


**Tags:** Depth-First Search, Breadth-First Search, Array, Matrix

**Difficulty:** Easy

## 思路

``` python3
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
```

[title]: https://leetcode-cn.com/problems/island-perimeter
