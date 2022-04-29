# [Find K-Length Substrings With No Repeated Characters][title]

## Description

给你一个字符串 `S`，找出所有长度为 `K` 且不含重复字符的子串，请你返回全部满足要求的子串的  **数目** 。



**示例 1：**
            **输入：** S = "havefunonleetcode", K = 5    **输出：** 6    **解释：**    这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。    

**示例 2：**
            **输入：** S = "home", K = 5    **输出：** 0    **解释：**    注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。



**提示：**

  1. `1 <= S.length <= 10^4`
  2. `S` 中的所有字符均为小写英文字母
  3. `1 <= K <= 10^4`


**Tags:** Hash Table, String, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/find-k-length-substrings-with-no-repeated-characters
