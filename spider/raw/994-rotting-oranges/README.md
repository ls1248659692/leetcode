# [Rotting Oranges][title]

## Description

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

  * 值 `0` 代表空单元格；
  * 值 `1` 代表新鲜橘子；
  * 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子  **周围  4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 _直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回  `-1`_ 。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/16/oranges.png)**
            **输入：** grid = [[2,1,1],[1,1,0],[0,1,1]]    **输出：** 4    

**示例 2：**
            **输入：** grid = [[2,1,1],[0,1,1],[1,0,1]]    **输出：** -1    **解释：** 左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。    

**示例 3：**
            **输入：** grid = [[0,2]]    **输出：** 0    **解释：** 因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。    



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 10`
  * `grid[i][j]` 仅为 `0`、`1` 或 `2`


**Tags:** Breadth-First Search, Array, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        g,m,n = grid,len(grid),len(grid[0])
        bad=[(i,j) for i in range(m) for j in range(n) if g[i][j]==2]
        aset,tset,sec=set(bad),set(bad),0
        while aset:
            _aset,aset=set(aset),set()
            for i,j in _aset:
                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    ii,jj=i+x,j+y
                    if 0<=ii<m and 0<=jj<n and g[ii][jj]==1 and (ii,jj) not in tset:
                        aset.add((ii,jj))
            if aset: sec+=1
            for pt in aset:tset.add(pt)
        return -1 if [(i,j) for i in range(m) for j in range(n) if g[i][j]==1 and (i,j) not in tset] else sec
```

[title]: https://leetcode-cn.com/problems/rotting-oranges
