# [Minimum Path Cost in a Hidden Grid][title]

## Description

这是一个交互问题。

有一个机器人存在于网格中，你需要通过不断尝试使他从初始单元到达目标单元。网格的规格为m x n，并且每个单元的属性值要不为空，要不已被占用。题目
**保证** 初始网格和目标网格不同且均为空。

每个单元格都有 **消耗** 值，你需要在每次 **移动** 至此单元格后支付该费用。在机器人启动前，初始单元的费用不被计算在内。

你需要找到机器人移动至目标网格的最小总消耗。但可惜的是你并 **不知道**
网格的尺寸、初始单元和目标单元。你只允许通过询问`GridMaster`类获得信息。

`GridMaster`类存在以下功能：

  * `boolean canMove(char direction)` 当机器人可以向这个方向移动时，返回`true`；反之返回`false`。
  * `int move(char direction)` 沿该方向移动机器人，并返回移动到该单元的消耗值。如果此移动将机器人移动到被占有的单元格或离开网格，则移动将被 **忽略** ，机器人将保持在相同的位置，函数将返回`-1`。
  * `boolean isTarget()` ：如果机器人当前位于目标单元格上，则返回`true`；反之返回 `false` 。

请注意，上述函数中的方向应该是`{ 'U'、'D'、'L'、'R' }`中的字符，分别表示向上、向下、左和右方向。

返回使机器人从其初始起始单元到目标单元的 **最小总消耗** 。如果单元格之间不存在有效路径，则返回`-1`。

**测试实例:**

测试输入一个大小为`m x n`的二维数组 `grid` 和四个`int`型参数 `r1`, `c1`, `r2`, 和 `c2` :

  * `grid[i][j] == 0` 表示网格 `(i, j)` 已被占用。
  * `grid[i][j] >= 1` 表示网格单元 `(i, j)` 为空并且 `grid[i][j]` 的值为移动至此网格的成本值。
  * `(r1, c1)` 为初始单元。
  * `(r2, c2)` 为目标单元。

请注意，你将无法在你的代码中获知这些信息。

**示例 1:**
            **输入:** grid = [[2,3],[1,1]], r1 = 0, c1 = 1, r2 = 1, c2 = 0    **输出:** 2    **解释:** 其中一种可能路径描述如下：    机器人最开始站在单元格 (0, 1) ，用 3 表示    - master.canMove('U') 返回 false    - master.canMove('D') 返回 true    - master.canMove('L') 返回 true    - master.canMove('R') 返回 false    - master.move('L') 机器人移动到单元格 (0, 0) 并返回 2    - master.isTarget() 返回 false    - master.canMove('U') 返回 false    - master.canMove('D') 返回 true    - master.canMove('L') 返回 false    - master.canMove('R') 返回 true    - master.move('D') 机器人移动到单元格 (1, 0) 并返回 1    - master.isTarget() 返回 true    - master.move('L') 机器人不移动并返回 -1    - master.move('R') 机器人移动到单元格 (1, 1) 并返回 1    现在我们知道了机器人达到目标单元(1, 0)的最小消耗成本为2。 

**示例 2:**
            **输入:** grid = [[0,3,1],[3,4,2],[1,2,0]], r1 = 2, c1 = 0, r2 = 0, c2 = 2    **输出:** 9    **解释:** 最小消耗路径为 (2,0) -> (2,1) -> (1,1) -> (1,2) -> (0,2).    

**示例 3:**
            **输入:** grid = [[1,0],[0,1]], r1 = 0, c1 = 0, r2 = 1, c2 = 1    **输出:** -1    **解释:** 不存在可使机器人到达目标单元的路径。    

**提示:**

  * `1 <= n, m <= 100`
  * `m == grid.length`
  * `n == grid[i].length`
  * `0 <= grid[i][j] <= 100`


**Tags:** Depth-First Search, Breadth-First Search, Graph, Interactive, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-path-cost-in-a-hidden-grid
