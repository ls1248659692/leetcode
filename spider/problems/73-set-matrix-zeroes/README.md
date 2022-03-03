# [Set Matrix Zeroes][title]

## Description

给定一个 ` _m_ x _n_` 的矩阵，如果一个元素为 **0** ，则将其所在行和列的所有元素都设为 **0** 。请使用
**[原地](http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)** 算法
**。**



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
            **输入：** matrix = [[1,1,1],[1,0,1],[1,1,1]]    **输出：** [[1,0,1],[0,0,0],[1,0,1]]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
            **输入：** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]    **输出：** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]    



**提示：**

  * `m == matrix.length`
  * `n == matrix[0].length`
  * `1 <= m, n <= 200`
  * `-231 <= matrix[i][j] <= 231 - 1`



**进阶：**

  * 一个直观的解决方案是使用  `O( _m_ _n_ )` 的额外空间，但这并不是一个好的解决方案。
  * 一个简单的改进方案是使用 `O( _m_  +  _n_ )` 的额外空间，但这仍然不是最好的解决方案。
  * 你能想出一个仅使用常量空间的解决方案吗？


**Tags:** Array, Hash Table, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/set-matrix-zeroes
