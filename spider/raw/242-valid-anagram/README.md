# [Valid Anagram][title]

## Description

给定两个字符串 `_s_` 和 `_t_` ，编写一个函数来判断 `_t_` 是否是 `_s_` 的字母异位词。

**注意：** 若 `_s_` 和 `_t_` __ 中每个字符出现的次数都相同，则称 `_s_` 和 `_t_` __ 互为字母异位词。

**示例 1:**
            **输入:** _s_ = "anagram", _t_ = "nagaram"    **输出:** true    

**示例 2:**
            **输入:** _s_ = "rat", _t_ = "car"    **输出:** false

**提示:**

  * `1 <= s.length, t.length <= 5 * 104`
  * `s` 和 `t` 仅包含小写字母

**进阶:** 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


**Tags:** Hash Table, String, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s))==sorted(list(t))
```

[title]: https://leetcode-cn.com/problems/valid-anagram
