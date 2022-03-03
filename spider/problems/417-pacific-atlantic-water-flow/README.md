# [Pacific Atlantic Water Flow][title]

## Description

有一个 `m × n` 的长方形岛屿，与 **太平洋** 和 **大西洋** 相邻。  **“太平洋”  **处于大陆的左边界和上边界，而
**“大西洋”** 处于大陆的右边界和下边界。

这个岛被分割成一个个方格网格。给定一个 `m x n` 的整数矩阵 `heights` ， `heights[r][c]` 表示坐标 `(r, c)`
上单元格 **高于海平面的高度** 。

岛上雨水较多，如果相邻小区的高度 **小于或等于** 当前小区的高度，雨水可以直接向北、南、东、西流向相邻小区。水可以从海洋附近的任何细胞流入海洋。

返回 _网格坐标`result` 的 **2D列表** ，其中 `result[i] = [ri, ci]` 表示雨水可以从单元格 `(ri, ci)`
流向 **太平洋和大西洋**_ 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)
            **输入:** heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]    **输出:** [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]    

**示例 2：**
            **输入:** heights = [[2,1],[1,2]]    **输出:** [[0,0],[0,1],[1,0],[1,1]]    



**提示：**

  * `m == heights.length`
  * `n == heights[r].length`
  * `1 <= m, n <= 200`
  * `0 <= heights[r][c] <= 105`


**Tags:** Depth-First Search, Breadth-First Search, Array, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/pacific-atlantic-water-flow
