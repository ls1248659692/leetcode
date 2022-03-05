# [Add Digits][title]

## Description

给定一个非负整数 `num`，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。



**示例 1:**
            **输入:** num = ****38    **输出:** 2     **解释:** 各位相加的过程为 **：** 38 --> 3 + 8 --> 11    11 --> 1 + 1 --> 2    由于 2 是一位数，所以返回 2。    

**示例 1:**
            **输入:** num = **** 0    **输出:** 0



**提示：**

  * `0 <= num <= 231 - 1`



**进阶：** 你可以不使用循环或者递归，在 `O(1)` 时间复杂度内解决这个问题吗？


**Tags:** Math, Number Theory, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def addDigits(self, num: int) -> int:
        sn= str(num)
        while len(sn)>1:
            sn = str(sum(int(e)for e in sn))
        return int(sn)
```

[title]: https://leetcode-cn.com/problems/add-digits
