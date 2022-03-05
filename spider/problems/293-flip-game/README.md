# [Flip Game][title]

## Description

你和朋友玩一个叫做「翻转游戏」的游戏。游戏规则如下：

给你一个字符串 `currentState` ，其中只含 `'+'` 和 `'-'` 。你和朋友轮流将 **连续** 的两个 `"++"` 反转成
`"--"` 。当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。

计算并返回 **一次有效操作** 后，字符串 `currentState` 所有的可能状态，返回结果可以按 **任意顺序**
排列。如果不存在可能的有效操作，请返回一个空列表 `[]` 。

**示例 1：**
            **输入：** currentState = "++++"    **输出：** ["--++","+--+","++--"]    

**示例 2：**
            **输入：** currentState = "+"    **输出：** []    

**提示：**

  * `1 <= currentState.length <= 500`
  * `currentState[i]` 不是 `'+'` 就是 `'-'`


**Tags:** String

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/flip-game
