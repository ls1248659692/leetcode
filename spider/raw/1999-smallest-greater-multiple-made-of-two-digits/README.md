# [Smallest Greater Multiple Made of Two Digits][title]

## Description

给你三个整数, `k`, `digit1`和 `digit2`, 你想要找到满足以下条件的 **最小** 整数：

  * **大于**`k` 且是 `k` 的 **倍数**
  * **仅由**`digit1` 和 `digit2` 组成，即 **每一位数** 均是 `digit1` 或 `digit2`

请你返回 ******最小的满足这两个条件的整数** ，如果不存在这样的整数，或者最小的满足这两个条件的整数不在32位整数范围（0~`231-1`），就返回
`-1` 。



**示例 1：**
            **输入：** k = 2, digit1 = 0, digit2 = 2    **输出：** 20    **解释：**    20 是第一个仅有数字0和2组成的，比2大且是2的倍数的整数。    

**示例 2：**
            **输入：** k = 3, digit1 = 4, digit2 = 2    **输出：** 24    **解释：**    24 是第一个仅有数字 2 和 4 组成的，比 3 大且是 3 的倍数的整数。

**示例 3：**
            **输入：** k = 2, digit1 = 0, digit2 = 0    **输出：** -1    **解释：** 不存在仅由 0 组成的比 2 大且是 2 的倍数的整数，因此返回 -1 。    



**提示：**

  * `1 <= k <= 1000`
  * `0 <= digit1 <= 9`
  * `0 <= digit2 <= 9`


**Tags:** 

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/smallest-greater-multiple-made-of-two-digits
