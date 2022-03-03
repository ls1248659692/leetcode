# [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix][title]

## Description

给你一个 `m x n` 的二进制矩阵 `mat`。每一步，你可以选择一个单元格并将它反转（反转表示 `0` 变 `1` ，`1` 变 `0`
）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。相邻的两个单元格共享同一条边。

请你返回将矩阵 `mat` 转化为全零矩阵的 _最少反转次数_ ，如果无法转化为全零矩阵，请返回 `-1` 。

**二进制矩阵**  的每一个格子要么是 `0` 要么是 `1` 。

**全零矩阵**  是所有格子都为 `0` 的矩阵。



**示例  1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/12/13/matrix.png)
            **输入：** mat = [[0,0],[0,1]]    **输出：** 3    **解释：** 一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。    

**示例 2：**
            **输入：** mat = [[0]]    **输出：** 0    **解释：** 给出的矩阵是全零矩阵，所以你不需要改变它。    

**示例 3：**
            **输入：** mat = [[1,0,0],[1,0,0]]    **输出：** -1    **解释：** 该矩阵无法转变成全零矩阵    



**提示：**

  * `m == mat.length`
  * `n == mat[0].length`
  * `1 <= m <= 3`
  * `1 <= n <= 3`
  * `mat[i][j]` 是 0 或 1 。


**Tags:** Bit Manipulation, Breadth-First Search, Array, Matrix

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
