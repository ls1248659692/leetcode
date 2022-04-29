# [Substrings That Begin and End With the Same Letter][title]

## Description

给你一个仅由小写英文字母组成的，  下标从 `0` 开始的字符串 `s` 。返回 `s` 中以相同字符开头和结尾的子字符串总数。

子字符串是字符串中连续的非空字符序列。



**示例 1：**
            **输入：** s = "abcba"    **输出：** 7    **解释：**    以相同字母开头和结尾的长度为 1 的子串是："a"、"b"、"c"、"b" 和 "a" 。    以相同字母开头和结尾的长度为 3 的子串是："bcb" 。    以相同字母开头和结尾的长度为 5 的子串是："abcba" 。    

**示例 2：**
            **输入：** s = "abacad"    **输出：** 9    **解释：**    以相同字母开头和结尾的长度为 1 的子串是："a"、"b"、"a"、"c"、"a" 和 "d" 。    以相同字母开头和结尾的长度为 3 的子串是："aba" 和 "aca" 。    以相同字母开头和结尾的长度为 5 的子串是："abaca" 。    

**示例 3：**
            **输入：** s = "a"    **输出：** 1    **解释：**    只有一个，以相同字母开头和结尾的长度为 1 的子串是："a"。    



**提示：**

  * `1 <= s.length <= 105`
  * `s` 仅包含小写英文字母。


**Tags:** Hash Table, Math, String, Counting, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/substrings-that-begin-and-end-with-the-same-letter
