# [Power of Three][title]

## Description

给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 `true` ；否则，返回 `false` 。

整数 `n` 是 3 的幂次方需满足：存在整数 `x` 使得 `n == 3x`



**示例 1：**
            **输入：** n = 27    **输出：** true    

**示例 2：**
            **输入：** n = 0    **输出：** false    

**示例 3：**
            **输入：** n = 9    **输出：** true    

**示例 4：**
            **输入：** n = 45    **输出：** false    



**提示：**

  * `-231 <= n <= 231 - 1`



**进阶：** 你能不使用循环或者递归来完成本题吗？


**Tags:** Recursion, Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        tli=[1]
        while tli[-1]<2**31: tli.append(tli[-1]*3)
        return n in tli
```

[title]: https://leetcode-cn.com/problems/power-of-three
