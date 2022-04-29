# [Minimum Number of Swaps to Make the Binary String Alternating][title]

## Description

给你一个二进制字符串 `s` ，现需要将其转化为一个 **交替字符串** 。请你计算并返回转化所需的 **最小** 字符交换次数，如果无法完成转化，返回
__`-1` __ 。

**交替字符串** 是指：相邻字符之间不存在相等情况的字符串。例如，字符串 `"010"` 和 `"1010"` 属于交替字符串，但 `"0100"`
不是。

任意两个字符都可以进行交换， **不必相邻** 。

**示例 1：**
            **输入：** s = "111000"    **输出：** 1    **解释：** 交换位置 1 和 4："1 _ **1**_ 10 _ **0**_ 0" -> "1 _ **0**_ 10 _ **1**_ 0" ，字符串变为交替字符串。    

**示例 2：**
            **输入：** s = "010"    **输出：** 0    **解释：** 字符串已经是交替字符串了，不需要交换。    

**示例 3：**
            **输入：** s = "1110"    **输出：** -1    

**提示：**

  * `1 <= s.length <= 1000`
  * `s[i]` 的值为 `'0'` 或 `'1'`


**Tags:** Greedy, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating
