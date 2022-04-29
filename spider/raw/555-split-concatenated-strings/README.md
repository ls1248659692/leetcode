# [Split Concatenated Strings][title]

## Description

给定一个字符串列表
`strs`，你可以将这些字符串连接成一个循环字符串，对于每个字符串，你可以选择是否翻转它。在所有可能的循环字符串中，你需要分割循环字符串（这将使循环字符串变成一个常规的字符串），然后找到字典序最大的字符串。

具体来说，要找到字典序最大的字符串，你需要经历两个阶段：

  1. 将所有字符串连接成一个循环字符串，你可以选择是否翻转某些字符串，并按照给定的顺序连接它们。
  2. 在循环字符串的某个位置分割它，这将使循环字符串从分割点变成一个常规的字符串。

你的工作是在所有可能的常规字符串中找到字典序最大的一个。



**示例 1:**
            **输入:** strs = ["abc","xyz"]    **输出:** "zyxcba"    **解释:** 你可以得到循环字符串 "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-"，其中 '-' 代表循环状态。     答案字符串来自第四个循环字符串， 你可以从中间字符 'a' 分割开然后得到 "zyxcba"。    

**示例 2:**
            **输入:** strs = ["abc"]    **输出:** "cba"    



**提示:**

  * `1 <= strs.length <= 1000`
  * `1 <= strs[i].length <= 1000`
  * `1 <= sum(strs[i].length) <= 1000`
  * `strs[i]` 只包含小写英文字母


**Tags:** Greedy, Array, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/split-concatenated-strings
