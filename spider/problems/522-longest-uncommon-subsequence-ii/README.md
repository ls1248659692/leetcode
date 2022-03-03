# [Longest Uncommon Subsequence II][title]

## Description

给定字符串列表 `strs` ，返回 _它们中 **最长的特殊序列**_ 。如果最长特殊序列不存在，返回 `-1` 。

**最长特殊序列** 定义如下：该序列为某字符串  **独有的最长子序列（即不能是其他字符串的子序列）** 。

 `s` 的  **子序列** 可以通过删去字符串 `s` 中的某些字符实现。

  * 例如，`"abc"` 是 `"aebdc"` 的子序列，因为您可以删除`"a _e_ b _d_ c"`中的下划线字符来得到 `"abc"` 。`"aebdc"`的子序列还包括`"aebdc"`、 `"aeb"` 和 "" (空字符串)。



**示例 1：**
            **输入:** strs = ["aba","cdc","eae"]    **输出:** 3    

**示例 2:**
            **输入:** strs = ["aaa","aaa","aa"]    **输出:** -1    



**提示:**

  * `2 <= strs.length <= 50`
  * `1 <= strs[i].length <= 10`
  * `strs[i]` 只包含小写英文字母


**Tags:** Array, Hash Table, Two Pointers, String, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/longest-uncommon-subsequence-ii
