# [Recursive Mulitply LCCI][title]

## Description

递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

**示例1:**
            **输入** ：A = 1, B = 10    **输出** ：10    

**示例2:**
            **输入** ：A = 3, B = 4    **输出** ：12    

**提示:**

  1. 保证乘法范围不会溢出


**Tags:** Bit Manipulation, Recursion, Math

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def multiply(self, A: int, B: int) -> int:
        def mup(a,b):
            if b<10: return a*b
            b,r,=b//10,b%10
            return mup(a,b)*10 +mup(a,r)
        return mup(A,B)
```

[title]: https://leetcode-cn.com/problems/recursive-mulitply-lcci
