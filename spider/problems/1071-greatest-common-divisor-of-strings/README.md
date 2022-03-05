# [Greatest Common Divisor of Strings][title]

## Description

对于字符串 `S` 和 `T`，只有在 `S = T + ... + T`（`T` 自身连接 1 次或多次）时，我们才认定 “`T` 能除尽 `S`”。

返回最长字符串 `X`，要求满足 `X` 能除尽 `str1` 且 `X` 能除尽 `str2`。

**示例 1：**
            **输入：** str1 = "ABCABC", str2 = "ABC"    **输出：** "ABC"    

**示例 2：**
            **输入：** str1 = "ABABAB", str2 = "ABAB"    **输出：** "AB"    

**示例 3：**
            **输入：** str1 = "LEET", str2 = "CODE"    **输出：** ""    

**提示：**

  1. `1 <= str1.length <= 1000`
  2. `1 <= str2.length <= 1000`
  3. `str1[i]` 和 `str2[i]` 为大写英文字母


**Tags:** Math, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        mi = str1 if len(str1)<len(str2) else str2
        ma = str1 if len(str1)>=len(str2) else str2
        x = mi
        while x and (ma.replace(x,'')!='' or mi.replace(x,'')!='') :
            x = x[1:]
        return x
```

[title]: https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
