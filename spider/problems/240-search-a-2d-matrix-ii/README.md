# [Search a 2D Matrix II][title]

## Description

编写一个高效的算法来搜索 ` _m_  x  _n_` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：

  * 每行的元素从左到右升序排列。
  * 每列的元素从上到下升序排列。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/11/25/searchgrid2.jpg)
            **输入：** matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5    **输出：** true    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/11/25/searchgrid.jpg)
            **输入：** matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20    **输出：** false    



**提示：**

  * `m == matrix.length`
  * `n == matrix[i].length`
  * `1 <= n, m <= 300`
  * `-109 <= matrix[i][j] <= 109`
  * 每行的所有元素从左到右升序排列
  * 每列的所有元素从上到下升序排列
  * `-109 <= target <= 109`


**Tags:** Array, Binary Search, Divide and Conquer, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for y in matrix:
            for x in y:
                if x == target:
                    return True
        return False
```

[title]: https://leetcode-cn.com/problems/search-a-2d-matrix-ii
