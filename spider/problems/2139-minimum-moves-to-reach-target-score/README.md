# [Minimum Moves to Reach Target Score][title]

## Description

你正在玩一个整数游戏。从整数 `1` 开始，期望得到整数 `target` 。

在一次行动中，你可以做下述两种操作之一：

  * **递增** ，将当前整数的值加 1（即， `x = x + 1`）。
  * **加倍** ，使当前整数的值翻倍（即，`x = 2 * x`）。

在整个游戏过程中，你可以使用 **递增** 操作 **任意** 次数。但是只能使用 **加倍** 操作 **至多** `maxDoubles` 次。

给你两个整数 `target` 和 `maxDoubles` ，返回从 1 开始得到 __`target` __ 需要的最少行动次数。



**示例 1：**
            **输入：** target = 5, maxDoubles = 0    **输出：** 4    **解释：** 一直递增 1 直到得到 target 。    

**示例 2：**
            **输入：** target = 19, maxDoubles = 2    **输出：** 7    **解释：** 最初，x = 1 。    递增 3 次，x = 4 。    加倍 1 次，x = 8 。    递增 1 次，x = 9 。    加倍 1 次，x = 18 。    递增 1 次，x = 19 。    

**示例 3：**
            **输入：** target = 10, maxDoubles = 4    **输出：** 4    **解释：**    最初，x = 1 。     递增 1 次，x = 2 。     加倍 1 次，x = 4 。     递增 1 次，x = 5 。     加倍 1 次，x = 10 。     



**提示：**

  * `1 <= target <= 109`
  * `0 <= maxDoubles <= 100`


**Tags:** Greedy, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-moves-to-reach-target-score
