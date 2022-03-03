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

[title]: https://leetcode-cn.com/problems/number-of-islands
