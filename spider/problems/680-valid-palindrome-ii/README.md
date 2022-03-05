# [Valid Palindrome II][title]

## Description

给定一个非空字符串 `s`， **最多** 删除一个字符。判断是否能成为回文字符串。

**示例 1:**
            **输入:** s = "aba"    **输出:** true    

**示例 2:**
            **输入:** s = "abca"    **输出:** true    **解释:** 你可以删除c字符。    

**示例 3:**
            **输入:** s = "abc"    **输出:** false

**提示:**

  * `1 <= s.length <= 105`
  * `s` 由小写英文字母组成


**Tags:** Greedy, Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def ispl(s):
            for i in range(1,len(s)//2+1):
                if s[i-1]!=s[-i]:return False
            return True
        if ispl(s):return True

        for i in range(1,len(s)//2+1):
            if s[i-1]==s[len(s)-i]:
                pass
            else:
                return ispl(s[:i-1]+s[i:]) or ispl(s[:len(s)-i]+s[len(s)-i+1:])
                #if ispl(s[:i]+s[i+1:]):return True
        return False

```

[title]: https://leetcode-cn.com/problems/valid-palindrome-ii
