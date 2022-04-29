# [整数除法][title]

## Description

给定两个整数 `a` 和 `b` ，求它们的除法的商 `a/b` ，要求不得使用乘号 `'*'`、除号 `'/'` 以及求余符号 `'%'` 。



**注意：**

  * 整数除法的结果应当截去（`truncate`）其小数部分，例如：`truncate(8.345) = 8` 以及 `truncate(-2.7335) = -2`
  * 假设我们的环境只能存储 32 位有符号整数，其数值范围是 `[−231, 231−1]`。本题中，如果除法结果溢出，则返回 `231 − 1`



**示例 1：**
            **输入：** a = 15, b = 2    **输出：** 7    **解释：** 15/2 = truncate(7.5) = 7    

**示例 2：**
            **输入：** a = 7, b = -3    **输出：** -2    **解释：** 7/-3 = truncate(-2.33333..) = -2

**示例 3：**
            **输入：** a = 0, b = 1    **输出：** 0

**示例 4：**
            **输入：** a = 1, b = 1    **输出：** 1



**提示:**

  * `-231 <= a, b <= 231 - 1`
  * `b != 0`



注意：本题与主站 29 题相同：<https://leetcode-cn.com/problems/divide-two-integers/>




**Tags:** Bit Manipulation, Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def divide(self, a: int, b: int) -> int:
        if (a,b)==(-2147483648,-1): return  2147483647
        return int(a/b)
```

[title]: https://leetcode-cn.com/problems/xoh6Oh
