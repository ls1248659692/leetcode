# [Shortest Path in a Hidden Grid][title]

## Description

这是一个 **交互式的问题。**

一个未知的网格里有一个机器人，你需要让机器人从起点走到终点。这个网格的大小是 `m x n`，网格中的每个位置只会是可通行和不可通行两种状态。题目
**保证** 机器人的起点和终点不同，且都是可通行的。

你需要找到起点到终点的最短路径，然而你 **不知道** 网格的大小、起点和终点。你只能向 `GridMaster` 对象查询。

`GridMaster`有这些方法：

  * `boolean canMove(char direction)` 当机器人能向对应方向移动时，返回 `true`，否则返回 `false`。
  * `void move(char direction)` 把机器人向这个方向移动。如果移动方向上是不可通行的或是网格的边界，则这次移动会被 **忽略** ，机器人会待在原地。
  * `boolean isTarget()` 如果机器人当前位于终点，返回 `true`，否则返回 `false`。

注意上述方法中的direction应该是 `{'U','D','L','R'}` 中的一个，分别代表上下左右四个方向。

返回机器人的初始位置到终点的最短距离。如果在起点和终点间没有路径联通，返回 `-1`。

**自定义测试用例**

测试用例是一个 `m x n` 的二维矩阵 `grid`，其中：

  * `grid[i][j] == -1` 表明机器人一开始位于位置 `(i, j)` （即起点）。
  * `grid[i][j] == 0` 表明位置 `(i, j)` 不可通行。
  * `grid[i][j] == 1` 表明位置 `(i, j)` 可以通行.
  * `grid[i][j] == 2` 表明位置 `(i, j)` 是终点.

`grid` 里恰有一个`-1` 和一个 `2`。记住在你的代码中，你对这些信息将 **一无所知** 。

**示例1：**
            **输入:** grid = [[1,2],[-1,0]]    **输出:** 2    **解释:** 一种可能的交互过程如下：    The robot is initially standing on cell (1, 0), denoted by the -1.    - master.canMove('U') 返回 true.    - master.canMove('D') 返回false.    - master.canMove('L') 返回 false.    - master.canMove('R') 返回 false.    - master.move('U') 把机器人移动到 (0, 0).    - master.isTarget() 返回 false.    - master.canMove('U') 返回 false.    - master.canMove('D') 返回 true.    - master.canMove('L') 返回 false.    - master.canMove('R') 返回 true.    - master.move('R') 把机器人移动到 (0, 1).    - master.isTarget() 返回 true.     我们现在知道终点是点 (0, 1)，而且最短的路径是2.    

**示例2:**
            **输入:** grid = [[0,0,-1],[1,1,1],[2,0,0]]    **输出:** 4    **解释:** 机器人和终点的最短路径长是4.

**示例3:**
            **输入:** grid = [[-1,0],[0,2]]    **输出:** -1    **解释:** 机器人和终点间没有可通行的路径.

**提示：**

  * `1 <= n, m <= 500`
  * `m == grid.length`
  * `n == grid[i].length`
  * `grid[i][j]` 只可能是 `-1`, `0`, `1` 或 `2`
  * `grid` 中 **有且只有一个** `-1`
  * `grid` 中 **有且只有一个** `2`


**Tags:** Depth-First Search, Breadth-First Search, Graph, Interactive

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shortest-path-in-a-hidden-grid
