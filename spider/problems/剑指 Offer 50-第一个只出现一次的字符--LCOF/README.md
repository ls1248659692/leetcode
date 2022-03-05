# [第一个只出现一次的字符  LCOF][title]

## Description

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

**示例 1:**
            输入：s = "abaccdeff"    输出：'b'    

**示例 2:**
            输入：s = ""     输出：' '    



**限制：**

`0 <= s 的长度 <= 50000`


**Tags:** Queue, Hash Table, String, Counting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def firstUniqChar(self, s: str) -> str:
        #tli = [ch for ch in s if s.count(ch)==1]
        for ch in s:
            if s.count(ch)==1:return ch
        return ' ' 
```

[title]: https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
