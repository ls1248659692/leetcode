# [Thousand Separator][title]

## Description

给你一个整数 `n`，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。



**示例 1：**
            **输入：** n = 987    **输出：** "987"    

**示例 2：**
            **输入：** n = 1234    **输出：** "1.234"    

**示例 3：**
            **输入：** n = 123456789    **输出：** "123.456.789"    

**示例 4：**
            **输入：** n = 0    **输出：** "0"    



**提示：**

  * `0 <= n < 2^31`


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) <= 3:
            return str(n)
        a = list(reversed(str(n)))
        cnt = 0
        for i in range(3,len(a),3):
            a.insert(i+cnt,'.')
            cnt += 1
     

        return ''.join(list(reversed(a)))
```

[title]: https://leetcode-cn.com/problems/thousand-separator
