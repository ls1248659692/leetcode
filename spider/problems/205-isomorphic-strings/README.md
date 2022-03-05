# [Isomorphic Strings][title]

## Description

给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。

如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。



**示例 1:**
            **输入：** s = "egg", t = "add"    **输出：** true    

**示例 2：**
            **输入：** s = "foo", t = "bar"    **输出：** false

**示例 3：**
            **输入：** s = "paper", t = "title"    **输出：** true



**提示：**

  * `1 <= s.length <= 5 * 104`
  * `t.length == s.length`
  * `s` 和 `t` 由任意有效的 ASCII 字符组成


**Tags:** Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(tup):
            srt = sorted(tup,key=lambda xx:xx[0])
            return sum([1 if (srt[i][0]== srt[i-1][0] and srt[i][1]!= srt[i-1][1]) or (srt[i][0]!= srt[i-1][0] and srt[i][1]== srt[i-1][1]) else 0 for i in range(1,len(srt))])==0
        return len(list(s))==len(list(t)) and check(zip(list(s),list(t))) and check(zip(list(t),list(s)))        
```

[title]: https://leetcode-cn.com/problems/isomorphic-strings
