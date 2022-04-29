# [Number of Matching Subsequences][title]

## Description

给定字符串 `s` 和字符串数组 `words`, 返回   _`words[i]` 中是`s`的子序列的单词个数_ 。

字符串的 **子序列** 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。

  * 例如， `“ace”` 是 `“abcde”` 的子序列。



**示例 1:**
            **输入:** s = "abcde", words = ["a","bb","acd","ace"]    **输出:** 3    **解释:** 有三个是 s 的子序列的单词: "a", "acd", "ace"。    

**Example 2:**
            **输入:** s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]    **输出:** 2    



**提示:**

  * `1 <= s.length <= 5 * 104`
  * `1 <= words.length <= 5000`
  * `1 <= words[i].length <= 50`
  * `words[i]`和 s 都只由小写字母组成。

​​​​


**Tags:** Trie, Hash Table, String, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-matching-subsequences
