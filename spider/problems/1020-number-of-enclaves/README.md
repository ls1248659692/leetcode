# [Number of Enclaves][title]

## Description

给你一个大小为 `m x n` 的二进制矩阵 `grid` ，其中 `0` 表示一个海洋单元格、`1` 表示一个陆地单元格。

一次 **移动** 是指从一个陆地单元格走到另一个相邻（ **上、下、左、右** ）的陆地单元格或跨过 `grid` 的边界。

返回网格中 **无法** 在任意次数的移动中离开网格边界的陆地单元格的数量。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg)
            **输入：** grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]    **输出：** 3    **解释：** 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg)
            **输入：** grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]    **输出：** 0    **解释：** 所有 1 都在边界上或可以到达边界。    



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 500`
  * `grid[i][j]` 的值为 `0` 或 `1`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Matrix

**Difficulty:** Medium

## 思路

``` python3
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
```

[title]: https://leetcode-cn.com/problems/number-of-enclaves
