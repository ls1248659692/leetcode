# [Maximum Product of the Length of Two Palindromic Substrings][title]

## Description

给你一个下标从 **0**  开始的字符串 `s` ，你需要找到两个 **不重叠** **的回文  **子字符串，它们的长度都必须为 **奇数**
，使得它们长度的乘积最大。

更正式地，你想要选择四个整数 `i` ，`j` ，`k` ，`l` ，使得 `0 <= i <= j < k <= l < s.length` ，且子字符串
`s[i...j]` 和 `s[k...l]` 都是回文串且长度为奇数。`s[i...j]` 表示下标从 `i` 到 `j` 且 **包含**
两端下标的子字符串。

请你返回两个不重叠回文子字符串长度的 **最大**  乘积。

**回文字符串**  指的是一个从前往后读和从后往前读一模一样的字符串。 **子字符串**  指的是一个字符串中一段连续字符。



**示例 1：**
            **输入：** s = "ababbb"    **输出：** 9    **解释：** 子字符串 "aba" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。    

**示例 2：**
            **输入：** s = "zaaaxbbby"    **输出：** 9    **解释：** 子字符串 "aaa" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。    



**提示：**

  * `2 <= s.length <= 105`
  * `s` 只包含小写英文字母。


**Tags:** String, Hash Function, Rolling Hash

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings
