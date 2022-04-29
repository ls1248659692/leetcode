# [Max Area of Island][title]

## Description

给你一个大小为 `m x n` 的二进制矩阵 `grid` 。

**岛屿**  是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在 **水平或者竖直的四个方向上** 相邻。你可以假设
`grid` 的四个边缘都被 `0`（代表水）包围着。

岛屿的面积是岛上值为 `1` 的单元格的数目。

计算并返回 `grid` 中最大的岛屿面积。如果没有岛屿，则返回面积为 `0` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)
            **输入：** grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]    **输出：** 6    **解释：** 答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。    

**示例 2：**
            **输入：** grid = [[0,0,0,0,0,0,0,0]]    **输出：** 0    



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 50`
  * `grid[i][j]` 为 `0` 或 `1`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Matrix

**Difficulty:** Medium

## 思路

``` python3
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
```

[title]: https://leetcode-cn.com/problems/max-area-of-island
