# [Perfect Number][title]

## Description

对于一个  **正整数** ，如果它和除了它自身以外的所有 **正因子** 之和相等，我们称它为 **「完美数」** 。

给定一个  **整数  **`n`， 如果是完美数，返回 `true`；否则返回 `false`。



**示例 1：**
            **输入：** num = 28    **输出：** true    **解释：** 28 = 1 + 2 + 4 + 7 + 14    1, 2, 4, 7, 和 14 是 28 的所有正因子。

**示例 2：**
            **输入：** num = 7    **输出：** false    



**提示：**

  * `1 <= num <= 108`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        factorsum = 0
        for j in range(1, int(num ** 0.5) + 1):
            if num % j == 0:
                factorsum = factorsum + j
                factorsum += num // j
        return factorsum == num * 2

```

[title]: https://leetcode-cn.com/problems/perfect-number
