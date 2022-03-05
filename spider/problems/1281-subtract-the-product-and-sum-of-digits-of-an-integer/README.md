# [Subtract the Product and Sum of Digits of an Integer][title]

## Description

给你一个整数 `n`，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。



**示例 1：**
            **输入：** n = 234    **输出：** 15     **解释：**    各位数之积 = 2 * 3 * 4 = 24     各位数之和 = 2 + 3 + 4 = 9     结果 = 24 - 9 = 15    

**示例 2：**
            **输入：** n = 4421    **输出：** 21    **解释：** 各位数之积 = 4 * 4 * 2 * 1 = 32     各位数之和 = 4 + 4 + 2 + 1 = 11     结果 = 32 - 11 = 21    



**提示：**

  * `1 <= n <= 10^5`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        add= 0
        multi = 1
        for i in n:
            add = int(i) + add
        for j in n:
            multi = int(j) * multi
        return multi-add
```

[title]: https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
