# [Valid Palindrome][title]

## Description

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

**说明：** 本题中，我们将空字符串定义为有效的回文串。

**示例 1:**
            **输入:** "A man, a plan, a canal: Panama"    **输出:** true    **解释：** "amanaplanacanalpanama" 是回文串    

**示例 2:**
            **输入:** "race a car"    **输出:** false    **解释：** "raceacar" 不是回文串    

**提示：**

  * `1 <= s.length <= 2 * 105`
  * 字符串 `s` 由 ASCII 字符组成


**Tags:** Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        sli = [ch for ch in s if 0<=ord(ch)-ord('a')<26 or ch in '01234567789']
        s = ''.join(sli)
        #print(s)
        #if len(s)==1:return False
        #for ch in ''_#@.,: ': s=s.replace(ch,'')
        for i in range(1,len(s)//2+1):
            if s[i-1]!=s[-i]:return False
        return True
        
```

[title]: https://leetcode-cn.com/problems/valid-palindrome
