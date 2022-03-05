# [Word Pattern][title]

## Description

给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的  **遵循  **指完全匹配，例如， `pattern` 里的每个字母和字符串 `str` ** **
中的每个非空单词之间存在着双向连接的对应规律。



**示例1:**
            **输入:** pattern = "abba", str = "dog cat cat dog"    **输出:** true

**示例 2:**
            **输入:** pattern = "abba", str = "dog cat cat fish"    **输出:** false

**示例 3:**
            **输入:** pattern = "aaaa", str = "dog cat cat dog"    **输出:** false



**提示:**

  * `1 <= pattern.length <= 300`
  * `pattern` 只包含小写英文字母
  * `1 <= s.length <= 3000`
  * `s` 只包含小写英文字母和 `' '`
  * `s`  **不包含** 任何前导或尾随对空格
  * `s` 中每个单词都被 **单个空格** 分隔


**Tags:** Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def wordPattern(self, pat: str, strg: str) -> bool:
        # def check(tup):
        #     s = sorted(tup)
        #     return sum([(s[i][0]== s[i-1][0] and s[i][1]!= s[i-1][1]) or (s[i][0]!= s[i-1][0] and s[i][1]== s[i-1][1]) for i in range(1,len(s))])==0
        # return len(list(pat)) == len(strg.split()) and check(zip(list(pat), strg.split())) and check(zip(strg.split(), list(pat)))

        p,s=list(pat),strg.split()
        return [dict(zip(p,s)).get(pp,None) for pp in p]==s and [dict(zip(s,p)).get(ss,None) for ss in s]==p
```

[title]: https://leetcode-cn.com/problems/word-pattern
