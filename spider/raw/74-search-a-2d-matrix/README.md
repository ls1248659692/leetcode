# [Search a 2D Matrix][title]

## Description

编写一个高效的算法来判断 `m x n` 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

  * 每行中的整数从左到右按升序排列。
  * 每行的第一个整数大于前一行的最后一个整数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
            **输入：** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3    **输出：** true    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/11/25/mat2.jpg)
            **输入：** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13    **输出：** false    

**提示：**

  * `m == matrix.length`
  * `n == matrix[i].length`
  * `1 <= m, n <= 100`
  * `-104 <= matrix[i][j], target <= 104`


**Tags:** Array, Binary Search, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        g,m,n= matrix,len(matrix),len(matrix[0])
        return target in [g[i][j]  for i in range(m) for j in range(n)]
```

[title]: https://leetcode-cn.com/problems/search-a-2d-matrix
