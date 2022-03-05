# [Base 7][title]

## Description

给定一个整数 `num`，将其转化为 **7 进制** ，并以字符串形式输出。



**示例 1:**
            **输入:** num = 100    **输出:** "202"    

**示例 2:**
            **输入:** num = -7    **输出:** "-10"    



**提示：**

  * `-107 <= num <= 107`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def convertToBase7(self, num: int) -> str:
        cli=[]
        s= '-' if num<0 else ''
        num = abs(num)
        while num>=7:
            cli.append(num%7)
            num = num//7
        cli.append(num)
        return s+''.join([str(e) for e in cli[::-1]])
```

[title]: https://leetcode-cn.com/problems/base-7
