# [Count Subarrays With More Ones Than Zeros][title]

## Description

给你一个只包含 `0` 和 `1` 的数组 `nums`，请返回 `1` 的数量 **大于**`0` 的数量的子数组的个数。由于答案可能很大，请返回答案对
`109 + 7`  **取余**  的结果。

一个 **子数组** 指的是原数组中连续的一个子序列。



**示例 1:**
            **输入:** nums = [0,1,1,0,1]    **输出:** 9    **解释:**    长度为 1 的、1 的数量大于 0 的数量的子数组有: [1], [1], [1]    长度为 2 的、1 的数量大于 0 的数量的子数组有: [1,1]    长度为 3 的、1 的数量大于 0 的数量的子数组有: [0,1,1], [1,1,0], [1,0,1]    长度为 4 的、1 的数量大于 0 的数量的子数组有: [1,1,0,1]    长度为 5 的、1 的数量大于 0 的数量的子数组有: [0,1,1,0,1]    

**示例 2:**
            **输入:** nums = [0]    **输出:** 0    **解释:**    没有子数组的 1 的数量大于 0 的数量。    

**示例 3:**
            **输入:** nums = [1]    **输出:** 1    **解释:**    长度为 1 的、1 的数量大于 0 的数量的子数组有: [1]    



**提示:**

  * `1 <= nums.length <= 105`
  * `0 <= nums[i] <= 1`


**Tags:** Binary Indexed Tree, Segment Tree, Array, Binary Search, Divide and Conquer, Ordered Set, Merge Sort

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/count-subarrays-with-more-ones-than-zeros
