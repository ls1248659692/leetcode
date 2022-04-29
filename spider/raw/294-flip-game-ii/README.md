# [Flip Game II][title]

## Description

你和朋友玩一个叫做「翻转游戏」的游戏。游戏规则如下：

给你一个字符串 `currentState` ，其中只含 `'+'` 和 `'-'` 。你和朋友轮流将  **连续** 的两个 `"++"` 反转成
`"--"` 。当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。默认每个人都会采取最优策略。

请你写出一个函数来判定起始玩家 **是否存在必胜的方案** ：如果存在，返回 `true` ；否则，返回 `false` 。



**示例 1：**
            **输入：** currentState = "++++"    **输出：** true    **解释：** 起始玩家可将中间的 "++" 翻转变为 "+--+" 从而得胜。

**示例 2：**
            **输入：** currentState = "+"    **输出：** false    



**提示：**

  * `1 <= currentState.length <= 60`
  * `currentState[i]` 不是 `'+'` 就是 `'-'`



**进阶：** 请推导你算法的时间复杂度。


**Tags:** Memoization, Math, Dynamic Programming, Backtracking, Game Theory

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/flip-game-ii
