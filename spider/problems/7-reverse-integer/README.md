# [Reverse Integer][title]

## Description

给你一个 32 位的有符号整数 `x` ，返回将 `x` 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 `[−231, 231 − 1]` ，就返回 0。

**假设环境不允许存储 64 位整数（有符号或无符号）。**

**示例 1：**
            **输入：** x = 123    **输出：** 321    

**示例 2：**
            **输入：** x = -123    **输出：** -321    

**示例 3：**
            **输入：** x = 120    **输出：** 21    

**示例 4：**
            **输入：** x = 0    **输出：** 0    

**提示：**

  * `-231 <= x <= 231 - 1`


**Tags:** Math

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        negpos =1
        if x_str[0]=='-': 
            negpos = -1
            x_str= x_str[1:]
        x_str_rev = ''.join([x_str[ii] for ii in range(len(x_str)-1,-1,-1)])
        #print(x_str_rev,2**31-1)
        x_rev = int(x_str_rev)*negpos
        return 0 if x_rev>2**31-1 else 0 if x_rev<-1*2**31 else x_rev
```

[title]: https://leetcode-cn.com/problems/reverse-integer
