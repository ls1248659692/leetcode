# [Integer Break][title]

## Description

给定一个正整数 `n` ，将其拆分为 `k` 个 **正整数** 的和（ `k >= 2` ），并使这些整数的乘积最大化。

返回 _你可以获得的最大乘积_  。



**示例 1:**
            **输入:** n = 2    **输出:** 1    **解释:** 2 = 1 + 1, 1 × 1 = 1。

**示例  2:**
            **输入:** n = 10    **输出:** 36    **解释:** 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。



**提示:**

  * `2 <= n <= 58`


**Tags:** Math, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:return 1
        if n==3:return 2
        else:
            if n%3==0: return math.prod([3]*(n//3))
            elif n%3==1: return math.prod([3]*(n//3-1)+[4])
            elif n%3==2: return math.prod([3]*(n//3)+[2])
```

[title]: https://leetcode-cn.com/problems/integer-break
