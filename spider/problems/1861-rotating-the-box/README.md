# [Rotating the Box][title]

## Description

给你一个 `m x n` 的字符矩阵 `box` ，它表示一个箱子的侧视图。箱子的每一个格子可能为：

  * `'#'` 表示石头
  * `'*'` 表示固定的障碍物
  * `'.'` 表示空位置

这个箱子被 **顺时针旋转 90 度** ，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力
**不会** 影响障碍物的位置，同时箱子旋转不会产生 **惯性** ，也就是说石头的水平位置不会发生改变。

题目保证初始时 `box` 中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。

请你返回一个 __`n x m`的矩阵，表示按照上述旋转后，箱子内的结果。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png)
            **输入：** box = [["#",".","#"]]    **输出：** [["."],          ["#"],          ["#"]]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png)
            **输入：** box = [["#",".","*","."],                ["#","#","*","."]]    **输出：** [["#","."],          ["#","#"],          ["*","*"],          [".","."]]    

**示例 3：**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png)
            **输入：** box = [["#","#","*",".","*","."],                ["#","#","#","*",".","."],                ["#","#","#",".","#","."]]    **输出：** [[".","#","#"],          [".","#","#"],          ["#","#","*"],          ["#","*","."],          ["#",".","*"],          ["#",".","."]]    

**提示：**

  * `m == box.length`
  * `n == box[i].length`
  * `1 <= m, n <= 500`
  * `box[i][j]` 只可能是 `'#'` ，`'*'` 或者 `'.'` 。


**Tags:** Array, Two Pointers, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/rotating-the-box
