# [Number of Wonderful Substrings][title]

## Description

如果某个字符串中 **至多一个** 字母出现 **奇数** 次，则称其为 **最美** 字符串。

  * 例如，`"ccjjc"` 和 `"abab"` 都是最美字符串，但 `"ab"` 不是。

给你一个字符串 `word` ，该字符串由前十个小写英文字母组成（`'a'` 到 `'j'`）。请你返回 `word` 中 **最美非空子字符串** 的数目
_。_ 如果同样的子字符串在 __`word` 中出现多次，那么应当对 **每次出现** 分别计数 _。_

**子字符串** 是字符串中的一个连续字符序列。

**示例 1：**
            **输入：** word = "aba"    **输出：** 4    **解释：** 4 个最美子字符串如下所示：    - " **a** ba" -> "a"    - "a **b** a" -> "b"    - "ab **a** " -> "a"    - " **aba** " -> "aba"    

**示例 2：**
            **输入：** word = "aabb"    **输出：** 9    **解释：** 9 个最美子字符串如下所示：    - " **a** abb" -> "a"    - " **aa** bb" -> "aa"    - " **aab** b" -> "aab"    - " **aabb** " -> "aabb"    - "a **a** bb" -> "a"    - "a **abb** " -> "abb"    - "aa **b** b" -> "b"    - "aa **bb** " -> "bb"    - "aab **b** " -> "b"    

**示例 3：**
            **输入：** word = "he"    **输出：** 2    **解释：** 2 个最美子字符串如下所示：    - " **h** e" -> "h"    - "h **e** " -> "e"    

**提示：**

  * `1 <= word.length <= 105`
  * `word` 由从 `'a'` 到 `'j'` 的小写英文字母组成


**Tags:** Bit Manipulation, Hash Table, String, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-wonderful-substrings
