# [Distinct Echo Substrings][title]

## Description

给你一个字符串 `text` ，请你返回满足下述条件的  **不同** 非空子字符串的数目：

  * 可以写成某个字符串与其自身相连接的形式（即，可以写为 `a + a`，其中 `a` 是某个字符串）。

例如，`abcabc` 就是 `abc` 和它自身连接形成的。



**示例 1：**
            **输入：** text = "abcabcabc"    **输出：** 3    **解释：** 3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。    

**示例 2：**
            **输入：** text = "leetcodeleetcode"    **输出：** 2    **解释：** 2 个子字符串为 "ee" 和 "leetcodeleetcode" 。    



**提示：**

  * `1 <= text.length <= 2000`
  * `text` 只包含小写英文字母。


**Tags:** Trie, String, Dynamic Programming, Sliding Window, Hash Function, Rolling Hash

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/distinct-echo-substrings
