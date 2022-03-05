# [Repeated Substring Pattern][title]

## Description

给定一个非空的字符串 `s` ，检查是否可以通过由它的一个子串重复多次构成。



**示例 1:**
            **输入:** s = "abab"    **输出:** true    **解释:** 可由子串 "ab" 重复两次构成。    

**示例 2:**
            **输入:** s = "aba"    **输出:** false    

**示例 3:**
            **输入:** s = "abcabcabcabc"    **输出:** true    **解释:** 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)    



**提示：**

  * `1 <= s.length <= 104`
  * `s` 由小写英文字母组成


**Tags:** String, String Matching

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        nn= len(s)
        if len(s)==1:return False
        if len(set(list(s)))==1:return True
        zys = [i for i in range(nn-1,1,-1)  if nn//i==nn/i]
        print(zys)
        for z in zys:
            if len(set([s[z*i:z*i+z] for i in range(nn//z)]))==1:return True
        return False
               
```

[title]: https://leetcode-cn.com/problems/repeated-substring-pattern
