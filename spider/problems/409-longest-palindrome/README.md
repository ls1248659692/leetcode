# [Longest Palindrome][title]

## Description

给定一个包含大写字母和小写字母的字符串 `s` ，返回  _通过这些字母构造成的 **最长的回文串**_  。

在构造过程中，请注意 **区分大小写** 。比如 `"Aa"` 不能当做一个回文字符串。



**示例 1:**
            **输入:** s = "abccccdd"    **输出:** 7    **解释:**    我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。    

**示例 2:**
            **输入:** s = "a"    **输入:** 1    

**示例 3:**
            **输入:** s = "bb"    **输入:** 2    



**提示:**

  * `1 <= s.length <= 2000`
  * `s` 只能由小写和/或大写英文字母组成


**Tags:** Greedy, Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def longestPalindrome(self, s: str) -> int:
        tli = [s.count(ch) for ch in set(list(s))]
        print(tli)
        return (1 if sum([el %2 for el in tli])>0 else 0) + sum([el//2 for el in tli])*2
```

[title]: https://leetcode-cn.com/problems/longest-palindrome
