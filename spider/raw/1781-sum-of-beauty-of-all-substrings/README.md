# [Sum of Beauty of All Substrings][title]

## Description

一个字符串的 **美丽值** 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。

  * 比方说，`"abaacc"` 的美丽值为 `3 - 1 = 2` 。

给你一个字符串 `s` ，请你返回它所有子字符串的 **美丽值** 之和。

**示例 1：**
            **输入：** s = "aabcb"    **输出：** 5    **解释：** 美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。

**示例 2：**
            **输入：** s = "aabcbaa"    **输出：** 17    

**提示：**

  * `1 <= s.length <= 500`
  * `s` 只包含小写英文字母。


**Tags:** Hash Table, String, Counting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/sum-of-beauty-of-all-substrings
