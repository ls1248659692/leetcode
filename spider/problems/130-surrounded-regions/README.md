# [Surrounded Regions][title]

## Description

给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` ，找到所有被 `'X'` 围绕的区域，并将这些区域里所有的
`'O'` 用 `'X'` 填充。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)
            **输入：** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]    **输出：** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]    **解释：** 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。    

**示例 2：**
            **输入：** board = [["X"]]    **输出：** [["X"]]    

**提示：**

  * `m == board.length`
  * `n == board[i].length`
  * `1 <= m, n <= 200`
  * `board[i][j]` 为 `'X'` 或 `'O'`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/surrounded-regions
