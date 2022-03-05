# [Digit Count in Range][title]

## Description

给定一个在 `0` 到 `9` 之间的整数 `d`，和两个正整数 `low` 和 `high` 分别作为上下界。返回 `d` 在 `low` 和
`high` 之间的整数中出现的次数，包括边界 `low` 和 `high`。



**示例 1：**
            **输入：** d = 1, low = 1, high = 13    **输出：** 6    **解释：**    数字 d=1 在 1,10,11,12,13 中出现 6 次。注意 d=1 在数字 11 中出现两次。    

**示例 2：**
            **输入：** d = 3, low = 100, high = 250    **输出：** 35    **解释：**    数字 d=3 在 103,113,123,130,131,...,238,239,243 出现 35 次。    



**提示：**

  1. `0 <= d <= 9`
  2. `1 <= low <= high <= 2×10^8`


**Tags:** Math, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/digit-count-in-range
