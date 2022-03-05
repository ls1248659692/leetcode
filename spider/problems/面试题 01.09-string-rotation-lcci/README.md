# [String Rotation LCCI][title]

## Description

字符串轮转。给定两个字符串`s1`和`s2`，请编写代码检查`s2`是否为`s1`旋转而成（比如，`waterbottle`是`erbottlewat`旋转后的字符串）。

**示例1:**
            **输入** ：s1 = "waterbottle", s2 = "erbottlewat"    **输出** ：True    

**示例2:**
            **输入** ：s1 = "aa", s2 = "aba"    **输出** ：False    

**提示：**

  1. 字符串长度在[0, 100000]范围内。

**说明:**

  1. 你能只调用一次检查子串的方法吗？


**Tags:** String, String Matching

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return s2 in s1+s1 and len(s1)==len(s2)
```

[title]: https://leetcode-cn.com/problems/string-rotation-lcci
