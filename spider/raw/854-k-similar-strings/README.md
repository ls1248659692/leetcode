# [K-Similar Strings][title]

## Description

字符串 `s1` 和 `s2` 是 **`k` 相似** 的(对于某些非负整数 `k` )，如果我们可以交换 `s1` 中两个字母的位置正好 `k`
次，使结果字符串等于 `s2` 。

给定两个字谜游戏 `s1` 和 `s2` ，返回 `s1` 和 `s2` 与 **`k` 相似 **的最小 `k` 。



**示例 1：**
            **输入：** s1 = "ab", s2 = "ba"    **输出：** 1    

**示例 2：**
            **输入：** s1 = "abc", s2 = "bca"    **输出：** 2    



**提示：**

  * `1 <= s1.length <= 20`
  * `s2.length == s1.length`
  * `s1` 和 `s2`  只包含集合 `{'a', 'b', 'c', 'd', 'e', 'f'}` 中的小写字母
  * `s2` 是 `s1` 的一个字谜


**Tags:** Breadth-First Search, String

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/k-similar-strings
