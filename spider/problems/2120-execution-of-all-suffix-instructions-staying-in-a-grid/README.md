# [Execution of All Suffix Instructions Staying in a Grid][title]

## Description

现有一个 `n x n` 大小的网格，左上角单元格坐标 `(0, 0)` ，右下角单元格坐标 `(n - 1, n - 1)` 。给你整数 `n`
和一个整数数组 `startPos` ，其中 `startPos = [startrow, startcol]` 表示机器人最开始在坐标为
`(startrow, startcol)` 的单元格上。

另给你一个长度为 `m` 、下标从 **0** 开始的字符串 `s` ，其中 `s[i]` 是对机器人的第 `i`
条指令：`'L'`（向左移动），`'R'`（向右移动），`'U'`（向上移动）和 `'D'`（向下移动）。

机器人可以从 `s` 中的任一第 `i` 条指令开始执行。它将会逐条执行指令直到 `s` 的末尾，但在满足下述条件之一时，机器人将会停止：

  * 下一条指令将会导致机器人移动到网格外。
  * 没有指令可以执行。

返回一个长度为 `m` 的数组 `answer` ，其中 `answer[i]` 是机器人从第 `i` 条指令 **开始**  ，可以执行的
**指令数目** 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/12/09/1.png)
            **输入：** n = 3, startPos = [0,1], s = "RRDDLU"    **输出：** [1,5,4,3,1,0]    **解释：** 机器人从 startPos 出发，并从第 i 条指令开始执行：    - 0: " _ **R**_ RDDLU" 在移动到网格外之前，只能执行一条 "R" 指令。    - 1:  " _ **RDDLU**_ " 可以执行全部五条指令，机器人仍在网格内，最终到达 (0, 0) 。    - 2:   " _ **DDLU**_ " 可以执行全部四条指令，机器人仍在网格内，最终到达 (0, 0) 。    - 3:    " _ **DLU**_ " 可以执行全部三条指令，机器人仍在网格内，最终到达 (0, 0) 。    - 4:     " _ **L**_ U" 在移动到网格外之前，只能执行一条 "L" 指令。    - 5:      "U" 如果向上移动，将会移动到网格外。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/12/09/2.png)
            **输入：** n = 2, startPos = [1,1], s = "LURD"    **输出：** [4,1,0,0]    **解释：**    - 0: " _ **LURD**_ "    - 1:  " _ **U**_ RD"    - 2:   "RD"    - 3:    "D"    

**示例 3：**

![](https://assets.leetcode.com/uploads/2021/12/09/3.png)
            **输入：** n = 1, startPos = [0,0], s = "LRUD"    **输出：** [0,0,0,0]    **解释：** 无论机器人从哪条指令开始执行，都会移动到网格外。    



**提示：**

  * `m == s.length`
  * `1 <= n, m <= 500`
  * `startPos.length == 2`
  * `0 <= startrow, startcol < n`
  * `s` 由 `'L'`、`'R'`、`'U'` 和 `'D'` 组成


**Tags:** String, Simulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid
