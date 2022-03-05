# [礼物的最大价值 LCOF][title]

## Description

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于
0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？



**示例 1:**
            **输入:**     [      [1,3,1],      [1,5,1],      [4,2,1]    ]    **输出:** 12    **解释:** 路径 1->3->5->2->1 可以拿到最多价值的礼物



提示：

  * `0 < grid.length <= 200`
  * `0 < grid[0].length <= 200`


**Tags:** Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        g,n,m = grid,len(grid),len(grid[0])
        zskip = lambda i,j,x: float('-inf') if not 0<=i<n or not 0<=j<m else x
        f=[[g[0][0]]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:continue
                f[i][j]= max(zskip(i,j-1,f[i][j-1]),zskip(i-1,j,f[i-1][j]))+g[i][j]
        return f[-1][-1]        
```

[title]: https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
