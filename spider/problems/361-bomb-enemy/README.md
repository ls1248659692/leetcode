# [Bomb Enemy][title]

## Description

给你一个大小为 `m x n` 的矩阵 `grid` ，其中每个单元格都放置有一个字符：

  * `'W'` 表示一堵墙
  * `'E'` 表示一个敌人
  * `'0'`（数字 0）表示一个空位

返回你使用 **一颗炸弹** 可以击杀的最大敌人数目。你只能把炸弹放在一个空位里。

由于炸弹的威力不足以穿透墙体，炸弹只能击杀同一行和同一列没被墙体挡住的敌人。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/27/bomb1-grid.jpg)
            **输入：** grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]    **输出：** 3    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/27/bomb2-grid.jpg)
            **输入：** grid = [["W","W","W"],["0","0","0"],["E","E","E"]]    **输出：** 1    



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 500`
  * `grid[i][j]` 可以是 `'W'`、`'E'` 或 `'0'`


**Tags:** Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/bomb-enemy
