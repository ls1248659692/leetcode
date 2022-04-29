# [Longest Line of Consecutive One in Matrix][title]

## Description

给定一个 `m x n` 的二进制矩阵 `mat` ** ** ，返回矩阵中最长的连续1线段。

这条线段可以是水平的、垂直的、对角线的或者反对角线的。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/long1-grid.jpg)
            **输入:**  mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]    **输出:** 3    

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/long2-grid.jpg)
            **输入:** mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]    **输出:** 4    



**提示:**

  * `m == mat.length`
  * `n == mat[i].length`
  * `1 <= m, n <= 104`
  * `1 <= m * n <= 104`
  * `mat[i][j]` 不是 `0` 就是 `1`.


**Tags:** Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/longest-line-of-consecutive-one-in-matrix
