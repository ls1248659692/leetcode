# [Transpose Matrix][title]

## Description

给你一个二维整数数组 `matrix`， 返回 `matrix` 的 **转置矩阵** 。

矩阵的 **转置** 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

![](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

**示例 1：**
            **输入：** matrix = [[1,2,3],[4,5,6],[7,8,9]]    **输出：** [[1,4,7],[2,5,8],[3,6,9]]    

**示例 2：**
            **输入：** matrix = [[1,2,3],[4,5,6]]    **输出：** [[1,4],[2,5],[3,6]]    

**提示：**

  * `m == matrix.length`
  * `n == matrix[i].length`
  * `1 <= m, n <= 1000`
  * `1 <= m * n <= 105`
  * `-109 <= matrix[i][j] <= 109`


**Tags:** Array, Matrix, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
```

[title]: https://leetcode-cn.com/problems/transpose-matrix
