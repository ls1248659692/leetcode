# [Maximum Side Length of a Square with Sum Less than or Equal to Threshold][title]

## Description

给你一个大小为 `m x n` 的矩阵 `mat` 和一个整数阈值 `threshold`。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 **0** 。  

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/15/e1.png)
            **输入：** mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4    **输出：** 2    **解释：** 总和小于或等于 4 的正方形的最大边长为 2，如图所示。    

**示例 2：**
            **输入：** mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1    **输出：** 0    

**示例 3：**
            **输入：** mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6    **输出：** 3    

**示例 4：**
            **输入：** mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184    **输出：** 2    

**提示：**

  * `1 <= m, n <= 300`
  * `m == mat.length`
  * `n == mat[i].length`
  * `0 <= mat[i][j] <= 10000`
  * `0 <= threshold <= 10^5`


**Tags:** Array, Binary Search, Matrix, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold
