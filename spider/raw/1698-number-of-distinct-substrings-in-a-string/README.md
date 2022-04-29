# [Number of Distinct Substrings in a String][title]

## Description

给定一个字符串 `s`，返回 `s` 的不同子字符串的个数。

字符串的 **子字符串** 是由原字符串删除开头若干个字符（可能是 0 个）并删除结尾若干个字符（可能是 0 个）形成的字符串。

**示例 1：**
            **输入：** s = "aabbaba"    **输出：** 21    **解释：** 不同子字符串的集合是 ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]    

**示例 2：**
            **输入：** s = "abcdefg"    **输出：** 28    

**提示：**

  * `1 <= s.length <= 500`
  * `s` 由小写英文字母组成。

**进阶：** 你可以以 `O(n)` 时间复杂度解决此问题吗？


**Tags:** Trie, String, Suffix Array, Hash Function, Rolling Hash

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-distinct-substrings-in-a-string
