# [Matrix Diagonal Sum][title]

## Description

给你一个正方形矩阵 `mat`，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。



**示例   1：**

![](https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png)
            **输入：** mat = [[ **1** ,2, **3** ],                [4, **5** ,6],                [ **7** ,8, **9** ]]    **输出：** 25    **解释：** 对角线的和为：1 + 5 + 9 + 3 + 7 = 25    请注意，元素 mat[1][1] = 5 只会被计算一次。    

**示例   2：**
            **输入：** mat = [[ **1** ,1,1, **1** ],                [1, **1** , **1** ,1],                [1, **1** , **1** ,1],                [ **1** ,1,1, **1** ]]    **输出：** 8    

**示例 3：**
            **输入：** mat = [[ **5** ]]    **输出：** 5    



**提示：**

  * `n == mat.length == mat[i].length`
  * `1 <= n <= 100`
  * `1 <= mat[i][j] <= 100`


**Tags:** Array, Matrix

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        m = 0 
        while m < len(mat):
            ans += mat[m][m] + mat[m][-m-1]
            m += 1
        if len(mat) % 2 == 1:
            ans -= mat[len(mat)//2][len(mat)//2]
        return ans
```

[title]: https://leetcode-cn.com/problems/matrix-diagonal-sum
