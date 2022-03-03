# [Number of Closed Islands][title]

## Description

二维矩阵 `grid` 由 `0` （土地）和 `1` （水）组成。岛是由最大的4个方向连通的 `0` 组成的群，封闭岛是一个 `完全`
由1包围（左、上、右、下）的岛。

请返回 _封闭岛屿_ 的数目。



**示例 1：**

![](https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png)
            **输入：** grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]    **输出：** 2    **解释：**    灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/07/sample_4_1610.png)
            **输入：** grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]    **输出：** 1    

**示例 3：**
            **输入：** grid = [[1,1,1,1,1,1,1],                 [1,0,0,0,0,0,1],                 [1,0,1,1,1,0,1],                 [1,0,1,0,1,0,1],                 [1,0,1,1,1,0,1],                 [1,0,0,0,0,0,1],                 [1,1,1,1,1,1,1]]    **输出：** 2    



**提示：**

  * `1 <= grid.length, grid[0].length <= 100`
  * `0 <= grid[i][j] <=1`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-closed-islands
