# [Minimum Deletions to Make String Balanced][title]

## Description

给你一个字符串 `s` ，它仅包含字符 `'a'` 和 `'b'`​​​​ 。

你可以删除 `s` 中任意数目的字符，使得 `s` **平衡** 。我们称 `s` **平衡的** 当不存在下标对 `(i,j)` 满足 `i < j` 且
`s[i] = 'b'` 同时 `s[j]= 'a'` 。

请你返回使 `s` **平衡** 的 **最少** 删除次数。

**示例 1：**
            **输入：** s = "aababbab"    **输出：** 2    **解释：** 你可以选择以下任意一种方案：    下标从 0 开始，删除第 2 和第 6 个字符（"aa **b** abb **a** b" -> "aaabbb"），    下标从 0 开始，删除第 3 和第 6 个字符（"aab **a** bb **a** b" -> "aabbbb"）。    

**示例 2：**
            **输入：** s = "bbaaaaabb"    **输出：** 2    **解释：** 唯一的最优解是删除最前面两个字符。    

**提示：**

  * `1 <= s.length <= 105`
  * `s[i]` 要么是 `'a'` 要么是 `'b'`​ **** 。​


**Tags:** Stack, String, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced
