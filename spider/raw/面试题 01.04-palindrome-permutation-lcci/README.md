# [Palindrome Permutation LCCI][title]

## Description

给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。



**示例1：**
            **输入： "**tactcoa"    **输出：** true（排列有"tacocat"、"atcocta"，等等）    




**Tags:** Bit Manipulation, Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ar = [s.count(ch) for ch in set(list(s)) if s.count(ch)%2!=0 ]
        return  len(ar)<=1 
        
        #for i in range(1,len(s)//2+1):
        #    if s[-i] !=s[i-1]: return False
        #return True
```

[title]: https://leetcode-cn.com/problems/palindrome-permutation-lcci
