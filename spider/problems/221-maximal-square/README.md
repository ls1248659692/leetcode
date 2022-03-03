# [Maximal Square][title]

## Description

在一个由 `'0'` 和 `'1'` 组成的二维矩阵内，找到只包含 `'1'` 的最大正方形，并返回其面积。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)
            **输入：** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]    **输出：** 4    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)
            **输入：** matrix = [["0","1"],["1","0"]]    **输出：** 1    

**示例 3：**
            **输入：** matrix = [["0"]]    **输出：** 0    

**提示：**

  * `m == matrix.length`
  * `n == matrix[i].length`
  * `1 <= m, n <= 300`
  * `matrix[i][j]` 为 `'0'` 或 `'1'`


**Tags:** Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximal-square
