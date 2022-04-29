# [Remove All Ones With Row and Column Flips][title]

## Description

You are given an `m x n` binary matrix `grid`.

In one operation, you can choose **any** row or column and flip each value in
that row or column (i.e., changing all `0`'s to `1`'s, and all `1`'s to
`0`'s).

Return `true` _if it is possible to remove all_`1` _' s from _`grid` using
**any** number of operations or `false` otherwise.



**Example 1:**

![](https://assets.leetcode.com/uploads/2022/01/03/image-20220103191300-1.png)
            Input: grid = [[0,1,0],[1,0,1],[0,1,0]]    Output: true    Explanation: One possible way to remove all 1's from grid is to:    - Flip the middle row    - Flip the middle column    

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/01/03/image-20220103181204-7.png)
            Input: grid = [[1,1,0],[0,0,0],[0,0,0]]    Output: false    Explanation: It is impossible to remove all 1's from grid.    

**Example 3:**

![](https://assets.leetcode.com/uploads/2022/01/03/image-20220103181224-8.png)
            Input: grid = [[0]]    Output: true    Explanation: There are no 1's in grid.    



**Constraints:**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 300`
  * `grid[i][j]` is either `0` or `1`.


**Tags:** Bit Manipulation, Array, Math, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/remove-all-ones-with-row-and-column-flips
