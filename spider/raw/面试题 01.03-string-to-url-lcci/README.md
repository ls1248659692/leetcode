# [String to URL LCCI][title]

## Description

URL化。编写一种方法，将字符串中的空格全部替换为`%20`。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用`Java`实现的话，请使用字符数组实现，以便直接在数组上操作。）

**示例 1：**
            **输入** ："Mr John Smith    ", 13    **输出** ："Mr%20John%20Smith"    

**示例 2：**
            **输入** ："               ", 5    **输出** ："%20%20%20%20%20"    

**提示：**

  * 字符串长度在 [0, 500000] 范围内。


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        nl = S.count(' ')*2+length
        return S[:length].replace(' ','%20')[:nl] if S.strip() else S[:length].replace(' ','%20')
```

[title]: https://leetcode-cn.com/problems/string-to-url-lcci
