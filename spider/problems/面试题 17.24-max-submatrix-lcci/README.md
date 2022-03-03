# [Max Submatrix LCCI][title]

## Description

给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 `[r1, c1, r2, c2]`，其中 `r1`, `c1` 分别代表子矩阵左上角的行号和列号，`r2`, `c2`
分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

**注意：** 本题相对书上原题稍作改动

**示例：**
            **输入：**[       [-1, **0** ],       [0,-1]    ]    **输出：** [0,1,0,1]    **解释：** 输入中标粗的元素即为输出所表示的矩阵



**说明：**

  * `1 <= matrix.length, matrix[0].length <= 200`


**Tags:** Array, Dynamic Programming, Matrix, Prefix Sum

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/max-submatrix-lcci
