# [Sqrt(x)][title]

## Description

给你一个非负整数 `x` ，计算并返回 `x` 的 **算术平方根** 。

由于返回类型是整数，结果只保留 **整数部分** ，小数部分将被 **舍去 。**

**注意：** 不允许使用任何内置指数函数和算符，例如 `pow(x, 0.5)` 或者 `x ** 0.5` 。



**示例 1：**
            **输入：** x = 4    **输出：** 2    

**示例 2：**
            **输入：** x = 8    **输出：** 2    **解释：** 8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。    



**提示：**

  * `0 <= x <= 231 - 1`


**Tags:** Math, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def mySqrt(self, x: int) -> int:
        #n = 0
        #while n * n <= x: 
        #    n = n +1
        for n in range(0,x+1):
            if n*n>=x:                
                return  n-1 if n*n>x else n

        
        
```

[title]: https://leetcode-cn.com/problems/sqrtx
