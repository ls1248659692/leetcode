# [Minimum Window Subsequence][title]

## Description

给定字符串 `S` and `T`，找出 `S` 中最短的（连续） **子串** `W` ，使得 `T` 是 `W` 的 **子序列** 。

如果 `S` 中没有窗口可以包含 `T` 中的所有字符，返回空字符串 `""`。如果有不止一个最短长度的窗口，返回开始位置最靠左的那个。

**示例 1：**
            **输入：**    S = "abcdebdde", T = "bde"    **输出：** "bcde"    **解释：**    "bcde" 是答案，因为它在相同长度的字符串 "bdde" 出现之前。    "deb" 不是一个更短的答案，因为在窗口中必须按顺序出现 T 中的元素。



**注：**

  * 所有输入的字符串都只包含小写字母。All the strings in the input will only contain lowercase letters.
  * `S` 长度的范围为 `[1, 20000]`。
  * `T` 长度的范围为 `[1, 100]`。




**Tags:** String, Dynamic Programming, Sliding Window

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-window-subsequence
