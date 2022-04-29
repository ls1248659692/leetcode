# [To Lower Case][title]

## Description

给你一个字符串 `s` ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

**示例 1：**
            **输入：** s = "Hello"    **输出：** "hello"    

**示例 2：**
            **输入：** s = "here"    **输出：** "here"    

**示例 3：**
            **输入：** s = "LOVELY"    **输出：** "lovely"    

**提示：**

  * `1 <= s.length <= 100`
  * `s` 由 ASCII 字符集中的可打印字符组成


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
```

[title]: https://leetcode-cn.com/problems/to-lower-case
