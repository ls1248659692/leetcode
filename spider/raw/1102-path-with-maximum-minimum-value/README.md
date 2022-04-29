# [Path With Maximum Minimum Value][title]

## Description

给定一个 `m x n` 的整数矩阵 `grid`，返回从 `(0,0)` 开始到 `(m - 1, n - 1)` 在四个基本方向上移动的路径的最大
**分数** 。

一条路径的 **分数** 是该路径上的最小值。

  * 例如，路径 `8 → 4 → 5 → 9` 的得分为 `4` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/08/05/maxgrid1.jpg)
            **输入：** grid = [[5,4,5],[1,2,6],[7,4,6]]    **输出：** 4    **解释：** 得分最高的路径用黄色突出显示。     

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/08/05/maxgrid2.jpg)
            **输入：** grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]    **输出：** 2

**示例 3：**

![](https://assets.leetcode.com/uploads/2021/08/05/maxgrid3.jpg)
            **输入：** grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]    **输出：** 3



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 100`
  * `0 <= grid[i][j] <= 109`




**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Matrix, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/path-with-maximum-minimum-value
