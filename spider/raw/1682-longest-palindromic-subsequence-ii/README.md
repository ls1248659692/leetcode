# [Longest Palindromic Subsequence II][title]

## Description

字符串 `s` 的某个子序列符合下列条件时，称为“ **好的回文子序列** ”：

  * 它是 `s` 的子序列。
  * 它是回文序列（反转后与原序列相等）。
  * 长度为 **偶数** 。
  * 除中间的两个字符外，其余任意两个连续字符不相等。

例如，若 `s = "abcabcabb"`，则 `"abba"` 可称为“好的回文子序列”，而 `"bcb"` （长度不是偶数）和 `"bbbb"`
（含有相等的连续字符）不能称为“好的回文子序列”。

给定一个字符串 `s`， 返回 __`s` 的 **最长“好的回文子序列”** 的 **长度** 。

**示例 1:**
            **输入:** s = "bbabab"    **输出:** 4    **解释:** s 的最长“好的回文子序列”是 "baab"。    

**示例 2:**
            **输入:** s = "dcbccacdb"    **输出:** 4    **解释:** The longest good palindromic subsequence of s is "dccd".    

**提示:**

  * `1 <= s.length <= 250`
  * `s` 包含小写英文字母。


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/longest-palindromic-subsequence-ii
