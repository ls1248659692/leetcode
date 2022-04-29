# [Number of Segments in a String][title]

## Description

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

**示例:**
            **输入:** "Hello, my name is John"    **输出:** 5    **解释:** 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。    


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countSegments(self, s: str) -> int:
        return len([wd for wd in s.split() if wd])
```

[title]: https://leetcode-cn.com/problems/number-of-segments-in-a-string
