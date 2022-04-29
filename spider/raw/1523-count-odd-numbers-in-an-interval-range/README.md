# [Count Odd Numbers in an Interval Range][title]

## Description

给你两个非负整数 `low` 和 `high` 。请你返回 _ _`low` __ 和 _ _`high` _ _ 之间（包括二者）奇数的数目。



**示例 1：**
            **输入：** low = 3, high = 7    **输出：** 3    **解释：** 3 到 7 之间奇数数字为 [3,5,7] 。

**示例 2：**
            **输入：** low = 8, high = 10    **输出：** 1    **解释：** 8 到 10 之间奇数数字为 [9] 。



**提示：**

  * `0 <= low <= high <= 10^9`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-high%2-low-low%2)//2  + high%2  + low%2 
```

[title]: https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range
