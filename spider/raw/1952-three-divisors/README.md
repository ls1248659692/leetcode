# [Three Divisors][title]

## Description

给你一个整数 `n` 。如果 `n` **恰好有三个正除数** ，返回 `true` __ ；否则，返回 __`false` 。

如果存在整数 `k` ，满足 `n = k * m` ，那么整数 `m` 就是 `n` 的一个 **除数** 。



**示例 1：**
            **输入：** n = 2    **输出：** false    **解释：** 2 只有两个除数：1 和 2 。

**示例 2：**
            **输入：** n = 4    **输出：** true    **解释：** 4 有三个除数：1、2 和 4 。    



**提示：**

  * `1 <= n <= 104`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isThree(self, n: int) -> bool:
        return math.sqrt(n) % 1 == 0 and [n % (1 + ii) for ii in range(int(math.sqrt(n)))].count(0) == 2        
```

[title]: https://leetcode-cn.com/problems/three-divisors
