# [Is Unique LCCI][title]

## Description

实现一个算法，确定一个字符串 `s` 的所有字符是否全都不同。

**示例 1：**
            **输入:** s = "leetcode"    **输出:** false     

**示例 2：**
            **输入:** s = "abc"    **输出:** true    

**限制：**

  * `0 <= len(s) <= 100 `
  * 如果你不使用额外的数据结构，会很加分。


**Tags:** Bit Manipulation, Hash Table, String, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(list(astr)))==len(astr)
```

[title]: https://leetcode-cn.com/problems/is-unique-lcci
