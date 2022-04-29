# [Number of Islands][title]

## Description

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

**示例 1：**
            **输入：** grid = [      ["1","1","1","1","0"],      ["1","1","0","1","0"],      ["1","1","0","0","0"],      ["0","0","0","0","0"]    ]    **输出：** 1    

**示例 2：**
            **输入：** grid = [      ["1","1","0","0","0"],      ["1","1","0","0","0"],      ["0","0","1","0","0"],      ["0","0","0","1","1"]    ]    **输出：** 3    

**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 300`
  * `grid[i][j]` 的值为 `'0'` 或 `'1'`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Matrix

**Difficulty:** Medium

## 思路

``` python3
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
```

[title]: https://leetcode-cn.com/problems/number-of-islands
