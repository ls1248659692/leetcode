# [最多删除一个字符得到回文][title]

## Description

给定一个非空字符串 `s`，请判断如果  **最多** 从字符串中删除一个字符能否得到一个回文字符串。



**示例 1:**
            **输入:** s = "aba"    **输出:** true    

**示例 2:**
            **输入:** s = "abca"    **输出:** true    **解释:** 可以删除 "c" 字符 或者 "b" 字符    

**示例 3:**
            **输入:** s = "abc"    **输出:** false



**提示:**

  * `1 <= s.length <= 105`
  * `s` 由小写英文字母组成



注意：本题与主站 680 题相同： <https://leetcode-cn.com/problems/valid-palindrome-ii/>


**Tags:** Greedy, Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def echo(ss):
            #print(ss)
            for ii in range(1,len(ss)//2+1):
                if ss[ii-1]!=ss[-ii]:return False
            return True
        
        if echo(s):return True
        badlt=0
        for i in range(1,len(s)//2+1):
           if s[i-1]!=s[-i]:
                badlt+=1
                return  echo(s[:i-1]+s[i:]) or echo(s[:-i]+(s[-i+1:] if i>1 else ''))
        return False       
```

[title]: https://leetcode-cn.com/problems/RQku0D
