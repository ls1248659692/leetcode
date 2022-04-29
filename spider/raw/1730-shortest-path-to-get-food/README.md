# [Shortest Path to Get Food][title]

## Description

你现在很饿，想要尽快找东西吃。你需要找到最短的路径到达一个食物所在的格子。

给定一个 `m x n` 的字符矩阵 `grid` ，包含下列不同类型的格子：

  * `'*'` 是你的位置。矩阵中 **有且只有一个**`'*'` 格子。
  * `'#'` 是食物。矩阵中可能存在 **多个** 食物。
  * `'O'` 是空地，你可以穿过这些格子。
  * `'X'` 是障碍，你不可以穿过这些格子。

返回你到任意食物的最短路径的长度。如果不存在你到任意食物的路径，返回 `-1`。

**示例 1:**

![](https://assets.leetcode.com/uploads/2020/09/21/img1.jpg)
            **输入：** grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]    **输出：** 3    **解释：** 要拿到食物，你需要走 3 步。

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/21/img2.jpg)
            **输入：** grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]    **输出：** -1    **解释：** 你不可能拿到食物。    

**示例 3:**

![](https://assets.leetcode.com/uploads/2020/09/21/img3.jpg)
            **输入:** grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]    **输出:** 6    **解释:** 这里有多个食物。拿到下边的食物仅需走 6 步。

**示例 4:**
            **输入:** grid = [["O","*"],["#","O"]]    **输出:** 2    

**示例 5:**
            **输入:** grid = [["X","*"],["#","X"]]    **输出:** -1

**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 200`
  * `grid[row][col]` 是 `'*'`、 `'X'`、 `'O'` 或 `'#'` 。
  * `grid` 中 **有且只有一个** `'*'` 。


**Tags:** Breadth-First Search, Array, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shortest-path-to-get-food
