# [Sparse Matrix Multiplication][title]

## Description

给定两个 [稀疏矩阵](https://baike.baidu.com/item/%E7%A8%80%E7%96%8F%E7%9F%A9%E9%98%B5)
：大小为 `m x k` 的稀疏矩阵 `mat1` 和大小为 `k x n` 的稀疏矩阵 `mat2` ，返回 `mat1 x mat2`
的结果。你可以假设乘法总是可能的。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/12/mult-grid.jpg)
            **输入：** mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]    **输出：** [[7,0,0],[-7,0,3]]    

**  示例 2:**
            **输入：** mat1 = [[0]], mat2 = [[0]]    **输出：** [[0]]    



**提示:**

  * `m == mat1.length`
  * `k == mat1[i].length == mat2.length`
  * `n == mat2[i].length`
  * `1 <= m, n, k <= 100`
  * `-100 <= mat1[i][j], mat2[i][j] <= 100`


**Tags:** Array, Hash Table, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/sparse-matrix-multiplication
