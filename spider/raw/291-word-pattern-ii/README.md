# [Word Pattern II][title]

## Description

给你一种规律 `pattern` 和一个字符串 `s`，请你判断 `s` 是否和 _ _`pattern` 的规律 **相匹配** 。

如果存在单个字符到字符串的 **双射映射** ，那么字符串 `s` 匹配 `pattern` ，即：如果`pattern`
中的每个字符都被它映射到的字符串替换，那么最终的字符串则为 `s` 。 **双射**
意味着映射双方一一对应，不会存在两个字符映射到同一个字符串，也不会存在一个字符分别映射到两个不同的字符串。



**示例 1：**
            **输入：** pattern = "abab", s = "redblueredblue"    **输出：** true    **解释：** 一种可能的映射如下：    'a' -> "red"    'b' -> "blue"

**示例 2：**
            **输入：** pattern = "aaaa", s = "asdasdasdasd"    **输出：** true    **解释：** 一种可能的映射如下：    'a' -> "asd"    

**示例 3：**
            **输入：** pattern = "aabb", s = "xyzabcxzyabc"    **输出：** false    



**提示：**

  * `1 <= pattern.length, s.length <= 20`
  * `pattern` 和 `s` 由小写英文字母组成


**Tags:** Hash Table, String, Backtracking

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/word-pattern-ii
