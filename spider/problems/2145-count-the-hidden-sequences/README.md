# [Count the Hidden Sequences][title]

## Description

给你一个下标从 **0**  开始且长度为 `n` 的整数数组 `differences` ，它表示一个长度为 `n + 1` 的  **隐藏**  数组
**相邻**  元素之间的  **差值**  。更正式的表述为：我们将隐藏数组记作 `hidden` ，那么 `differences[i] =
hidden[i + 1] - hidden[i]` 。

同时给你两个整数 `lower` 和 `upper` ，它们表示隐藏数组中所有数字的值都在 **闭**  区间 `[lower, upper]` 之间。

  * 比方说，`differences = [1, -3, 4]` ，`lower = 1` ，`upper = 6` ，那么隐藏数组是一个长度为 `4` 且所有值都在 `1` 和 `6` （包含两者）之间的数组。     * `[3, 4, 1, 5]` 和 `[4, 5, 2, 6]` 都是符合要求的隐藏数组。    * `[5, 6, 3, 7]` 不符合要求，因为它包含大于 `6` 的元素。    * `[1, 2, 3, 4]` 不符合要求，因为相邻元素的差值不符合给定数据。

请你返回 **符合**  要求的隐藏数组的数目。如果没有符合要求的隐藏数组，请返回 `0` 。



**示例 1：**
            **输入：** differences = [1,-3,4], lower = 1, upper = 6    **输出：** 2    **解释：** 符合要求的隐藏数组为：    - [3, 4, 1, 5]    - [4, 5, 2, 6]    所以返回 2 。    

**示例 2：**
            **输入：** differences = [3,-4,5,1,-2], lower = -4, upper = 5    **输出：** 4    **解释：** 符合要求的隐藏数组为：    - [-3, 0, -4, 1, 2, 0]    - [-2, 1, -3, 2, 3, 1]    - [-1, 2, -2, 3, 4, 2]    - [0, 3, -1, 4, 5, 3]    所以返回 4 。    

**示例 3：**
            **输入：** differences = [4,-7,2], lower = 3, upper = 6    **输出：** 0    **解释：** 没有符合要求的隐藏数组，所以返回 0 。    



**提示：**

  * `n == differences.length`
  * `1 <= n <= 105`
  * `-105 <= differences[i] <= 105`
  * `-105 <= lower <= upper <= 105`


**Tags:** Array, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/count-the-hidden-sequences
