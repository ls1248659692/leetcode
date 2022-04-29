# [Regions Cut By Slashes][title]

## Description

在由 `1 x 1` 方格组成的 `n x n` 网格 `grid` 中，每个 `1 x 1` 方块由 `'/'`、`'\'`
或空格构成。这些字符会将方块划分为一些共边的区域。

给定网格 `grid` 表示为一个字符串数组，返回 _区域的数量_ 。

请注意，反斜杠字符是转义的，因此 `'\'` 用 `'\\'` 表示。



**示例 1：**

![](https://assets.leetcode.com/uploads/2018/12/15/1.png)
            **输入：** grid = [" /","/ "]    **输出：** 2

**示例 2：**

![](https://assets.leetcode.com/uploads/2018/12/15/2.png)
            **输入：** grid = [" /","  "]    **输出：** 1    

**示例 3：**

![](https://assets.leetcode.com/uploads/2018/12/15/4.png)
            **输入：** grid = ["/\\","\\/"]    **输出：** 5    **解释：** 回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。    



**提示：**

  * `n == grid.length == grid[i].length`
  * `1 <= n <= 30`
  * `grid[i][j]` 是 `'/'`、`'\'`、或 `' '`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Graph

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/regions-cut-by-slashes
