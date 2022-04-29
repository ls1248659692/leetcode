# [Maximal Rectangle][title]

## Description

给定一个仅包含 `0` 和 `1` 、大小为 `rows x cols` 的二维二进制矩阵，找出只包含 `1` 的最大矩形，并返回其面积。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
            **输入：** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]    **输出：** 6    **解释：** 最大矩形如上图所示。    

**示例 2：**
            **输入：** matrix = []    **输出：** 0    

**示例 3：**
            **输入：** matrix = [["0"]]    **输出：** 0    

**示例 4：**
            **输入：** matrix = [["1"]]    **输出：** 1    

**示例 5：**
            **输入：** matrix = [["0","0"]]    **输出：** 0    



**提示：**

  * `rows == matrix.length`
  * `cols == matrix[0].length`
  * `1 <= row, cols <= 200`
  * `matrix[i][j]` 为 `'0'` 或 `'1'`


**Tags:** Stack, Array, Dynamic Programming, Matrix, Monotonic Stack

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/maximal-rectangle
