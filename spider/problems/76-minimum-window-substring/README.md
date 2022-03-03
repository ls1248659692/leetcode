# [Minimum Window Substring][title]

## Description

给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t`
所有字符的子串，则返回空字符串 `""` 。

**注意：**

  * 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
  * 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

**示例 1：**
            **输入：** s = "ADOBECODEBANC", t = "ABC"    **输出：** "BANC"    

**示例 2：**
            **输入：** s = "a", t = "a"    **输出：** "a"    

**示例 3:**
            **输入:** s = "a", t = "aa"    **输出:** ""    **解释:** t 中两个字符 'a' 均应包含在 s 的子串中，    因此没有符合条件的子字符串，返回空字符串。

**提示：**

  * `1 <= s.length, t.length <= 105`
  * `s` 和 `t` 由英文字母组成

**进阶：** 你能设计一个在 `o(n)` 时间内解决此问题的算法吗？


**Tags:** Hash Table, String, Sliding Window

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-window-substring
