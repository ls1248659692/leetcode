# [Subarrays with K Different Integers][title]

## Description

给定一个正整数数组 `nums`和一个整数 k ，返回 num 中 「 **好子数组」** _ _ 的数目。

如果 `nums` 的某个子数组中不同整数的个数恰好为 `k`，则称 `nums` 的这个连续、不一定不同的子数组为 **「** **好子数组 」** 。

  * 例如，`[1,2,3,1,2]` 中有 `3` 个不同的整数：`1`，`2`，以及 `3`。

**子数组** 是数组的 **连续** 部分。



**示例 1：**
            **输入：** nums = [1,2,1,2,3], k = 2    **输出：** 7    **解释：** 恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].    

**示例 2：**
            **输入：** nums = [1,2,1,3,4], k = 3    **输出：** 3    **解释：** 恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].    



**提示：**

  * `1 <= nums.length <= 2 * 104`
  * `1 <= nums[i], k <= nums.length`


**Tags:** Array, Hash Table, Counting, Sliding Window

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/subarrays-with-k-different-integers
