# [Number Of Corner Rectangles][title]

## Description

给定一个只包含 `0` 和 `1` 的 `m x n` 整数矩阵 `grid` ，返回 _其中 「 **角矩形 」** 的数量_ 。

一个 **「角矩形」** 是由四个不同的在矩阵上的 `1` 形成的轴对称的矩形。注意只有角的位置才需要为 `1`。

**注意：** 4 个 `1` 的位置需要是不同的。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/12/cornerrec1-grid.jpg)
            **输入：** grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]    **输出：** 1    **解释：** 只有一个角矩形，角的位置为 grid[1][2], grid[1][4], grid[3][2], grid[3][4]。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/06/12/cornerrec2-grid.jpg)
            **输入：** grid = [[1,1,1],[1,1,1],[1,1,1]]    **输出：** 9    **解释：** 这里有 4 个 2x2 的矩形，4 个 2x3 和 3x2 的矩形和 1 个 3x3 的矩形。    

**示例 3：**

![](https://assets.leetcode.com/uploads/2021/06/12/cornerrec3-grid.jpg)
            **输入：** grid = [[1,1,1,1]]    **输出：** 0    **解释：** 矩形必须有 4 个不同的角。    



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 200`
  * `grid[i][j]` 不是 `0` 就是 `1`
  * 网格中 `1` 的个数在 `[1, 6000]` 范围内


**Tags:** Array, Math, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-corner-rectangles
