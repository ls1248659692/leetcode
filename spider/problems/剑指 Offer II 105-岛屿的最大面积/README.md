# [岛屿的最大面积][title]

## Description

给定一个由 `0` 和 `1` 组成的非空二维数组 `grid` ，用来表示海洋岛屿地图。

一个  **岛屿**  是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在水平或者竖直方向上相邻。你可以假设
`grid` 的四个边缘都被 `0`（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 `0` 。



**示例 1:**

![](https://pic.leetcode-cn.com/1626667010-nSGPXz-image.png)
            **输入:** grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]    **输出:** 6    **解释:** 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

**示例 2:**
            **输入:** grid = [[0,0,0,0,0,0,0,0]]    **输出:** 0



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 50`
  * `grid[i][j] is either 0 or 1`



注意：本题与主站 695 题相同： <https://leetcode-cn.com/problems/max-area-of-island/>


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

[title]: https://leetcode-cn.com/problems/ZL6zAn
