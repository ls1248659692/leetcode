# [Rotate Image][title]

## Description

给定一个 _n  _×  _n_ 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在
**[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)**
旋转图像，这意味着你需要直接修改输入的二维矩阵。 **请不要** 使用另一个矩阵来旋转图像。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)
            **输入：** matrix = [[1,2,3],[4,5,6],[7,8,9]]    **输出：** [[7,4,1],[8,5,2],[9,6,3]]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)
            **输入：** matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]    **输出：** [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]    



**提示：**

  * `n == matrix.length == matrix[i].length`
  * `1 <= n <= 20`
  * `-1000 <= matrix[i][j] <= 1000`




**Tags:** Array, Math, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            matrix[i],  matrix[-1-i] = matrix[-1-i], matrix[i]
        for j in range(n):
            for k in range(j+1, n):
                matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]
```

[title]: https://leetcode-cn.com/problems/rotate-image
