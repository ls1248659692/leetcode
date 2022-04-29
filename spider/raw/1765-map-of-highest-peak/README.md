# [Map of Highest Peak][title]

## Description

给你一个大小为 `m x n` 的整数矩阵 `isWater` ，它代表了一个由 **陆地**  和 **水域**  单元格组成的地图。

  * 如果 `isWater[i][j] == 0` ，格子 `(i, j)` 是一个 **陆地**  格子。
  * 如果 `isWater[i][j] == 1` ，格子 `(i, j)` 是一个 **水域**  格子。

你需要按照如下规则给每个单元格安排高度：

  * 每个格子的高度都必须是非负的。
  * 如果一个格子是 **水域**  ，那么它的高度必须为 `0` 。
  * 任意相邻的格子高度差 **至多**  为 `1` 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）

找到一种安排高度的方案，使得矩阵中的最高高度值  **最大**  。

请你返回一个大小为 `m x n` 的整数矩阵 `height` ，其中 `height[i][j]` 是格子 `(i, j)`
的高度。如果有多种解法，请返回  **任意一个**  。



**示例 1：**

**![](https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82045-am.png)**
            **输入：** isWater = [[0,1],[0,0]]    **输出：** [[1,0],[2,1]]    **解释：** 上图展示了给各个格子安排的高度。    蓝色格子是水域格，绿色格子是陆地格。    

**示例 2：**

**![](https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82050-am.png)**
            **输入：** isWater = [[0,0,1],[1,0,0],[0,0,0]]    **输出：** [[1,1,0],[0,1,1],[1,2,2]]    **解释：** 所有安排方案中，最高可行高度为 2 。    任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。    



**提示：**

  * `m == isWater.length`
  * `n == isWater[i].length`
  * `1 <= m, n <= 1000`
  * `isWater[i][j]` 要么是 `0` ，要么是 `1` 。
  * 至少有 **1**  个水域格子。


**Tags:** Breadth-First Search, Array, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def max_link(r,c,hset):
            h= g[r][c]
            for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:      
                rr,cc,h1= r+i,c+j,h+1          
                if 0<=rr<m and 0<=cc<n and  h1<g[rr][cc]:
                    g[rr][cc]=h1
                    hset.add((rr,cc))

        g,m,n= isWater,len(isWater),len(isWater[0])
        m_n= m*n
        g = [ [0 if g[i][j] else m_n for j in range(n)] for i in range(m)]
        hset = [(i,j) for i in range(m) for j in range(n) if g[i][j]==0]
        for h in range(0,m_n+1):
            _hset,hset=set(hset),set()
            for r,c in _hset:
                max_link(r,c,hset)
        return g
```

[title]: https://leetcode-cn.com/problems/map-of-highest-peak
