# [Matrix Block Sum][title]

## Description

给你一个 `m x n` 的矩阵 `mat` 和一个整数 `k` ，请你返回一个矩阵 `answer` ，其中每个 `answer[i][j]`
是所有满足下述条件的元素 `mat[r][c]` 的和：

  * `i - k <= r <= i + k, `
  * `j - k <= c <= j + k` 且
  * `(r, c)` 在矩阵内。

**示例 1：**
            **输入：** mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1    **输出：** [[12,21,16],[27,45,33],[24,39,28]]    

**示例 2：**
            **输入：** mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2    **输出：** [[45,45,45],[45,45,45],[45,45,45]]    

**提示：**

  * `m == mat.length`
  * `n == mat[i].length`
  * `1 <= m, n, k <= 100`
  * `1 <= mat[i][j] <= 100`


**Tags:** Array, Matrix, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/matrix-block-sum
