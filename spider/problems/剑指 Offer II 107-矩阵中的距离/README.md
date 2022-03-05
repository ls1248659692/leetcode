# [矩阵中的距离][title]

## Description

给定一个由 `0` 和 `1` 组成的矩阵 `mat` ，请输出一个大小相同的矩阵，其中每一个格子是 `mat` 中对应位置元素到最近的 `0` 的距离。

两个相邻元素间的距离为 `1` 。



**示例 1：**

![](https://pic.leetcode-cn.com/1626667201-NCWmuP-image.png)
            **输入：** mat = **** [[0,0,0],[0,1,0],[0,0,0]]    **输出：** [[0,0,0],[0,1,0],[0,0,0]]    

**示例 2：**

![](https://pic.leetcode-cn.com/1626667205-xFxIeK-image.png)
            **输入：** mat = **** [[0,0,0],[0,1,0],[1,1,1]]    **输出：** [[0,0,0],[0,1,0],[1,2,1]]    



**提示：**

  * `m == mat.length`
  * `n == mat[i].length`
  * `1 <= m, n <= 104`
  * `1 <= m * n <= 104`
  * `mat[i][j] is either 0 or 1.`
  * `mat` 中至少有一个 `0 `



注意：本题与主站 542 题相同：<https://leetcode-cn.com/problems/01-matrix/>


**Tags:** Breadth-First Search, Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/2bCMpM
