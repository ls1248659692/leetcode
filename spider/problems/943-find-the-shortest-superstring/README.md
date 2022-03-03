# [Find the Shortest Superstring][title]

## Description

给定一个字符串数组 `words`，找到以 `words` 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中
**任意一个** 即可。

我们可以假设 `words` 中没有字符串是 `words` 中另一个字符串的子字符串。

**示例 1：**
            **输入：** words = ["alex","loves","leetcode"]    **输出：** "alexlovesleetcode"    **解释：** "alex"，"loves"，"leetcode" 的所有排列都会被接受。

**示例 2：**
            **输入：** words = ["catg","ctaagt","gcta","ttca","atgcatc"]    **输出：** "gctaagttcatgcatc"

**提示：**

  * `1 <= words.length <= 12`
  * `1 <= words[i].length <= 20`
  * `words[i]` 由小写英文字母组成
  * `words` 中的所有字符串 **互不相同**


**Tags:** Bit Manipulation, Array, String, Dynamic Programming, Bitmask

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/find-the-shortest-superstring
