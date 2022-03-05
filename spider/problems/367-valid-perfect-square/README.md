# [Valid Perfect Square][title]

## Description

给定一个 **正整数** `num` ，编写一个函数，如果 `num` 是一个完全平方数，则返回 `true` ，否则返回 `false` 。

**进阶：不要** 使用任何内置的库函数，如 `sqrt` 。

**示例 1：**
            **输入：** num = 16    **输出：** true    

**示例 2：**
            **输入：** num = 14    **输出：** false    

**提示：**

  * `1 <= num <= 2^31 - 1`


**Tags:** Math, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num in [i**2 for i in range(1,5*10**4)]
```

[title]: https://leetcode-cn.com/problems/valid-perfect-square
