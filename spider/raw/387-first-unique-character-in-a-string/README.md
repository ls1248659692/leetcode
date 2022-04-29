# [First Unique Character in a String][title]

## Description

给定一个字符串 `s` ，找到 _它的第一个不重复的字符，并返回它的索引_ 。如果不存在，则返回 `-1` 。



**示例 1：**
            **输入:** s = "leetcode"    **输出:** 0    

**示例 2:**
            **输入:** s = "loveleetcode"    **输出:** 2    

**示例 3:**
            **输入:** s = "aabb"    **输出:** -1    



**提示:**

  * `1 <= s.length <= 105`
  * `s` 只包含小写字母


**Tags:** Queue, Hash Table, String, Counting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i])==1: return i
        return -1
```

[title]: https://leetcode-cn.com/problems/first-unique-character-in-a-string
