# [Magic Squares In Grid][title]

## Description

`3 x 3` 的幻方是一个填充有  **从`1` 到 `9` ** 的不同数字的 `3 x 3` 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

给定一个由整数组成的`row x col` 的 `grid`，其中有多少个 `3 × 3` 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg)
            **输入:** grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]    **输出:** 1    **解释:**    下面的子矩阵是一个 3 x 3 的幻方：    ![](https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg)    而这一个不是：    ![](https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg)    总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。    

**示例 2:**
            **输出:** grid = [[8]]    **输入:** 0    



**提示:**

  * `row == grid.length`
  * `col == grid[i].length`
  * `1 <= row, col <= 10`
  * `0 <= grid[i][j] <= 15`


**Tags:** Array, Math, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/magic-squares-in-grid
