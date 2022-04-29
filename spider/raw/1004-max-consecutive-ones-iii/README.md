# [Max Consecutive Ones III][title]

## Description

给定一个二进制数组 `nums` 和一个整数 `k` ，如果可以翻转最多`k` 个 `0` ，则返回 _数组中连续`1` 的最大个数_ 。



**示例 1：**
            **输入：** nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2    **输出：** 6    **解释：** [1,1,1,0,0, **1** ,1,1,1,1, **1** ]    粗体数字从 0 翻转到 1，最长的子数组长度为 6。

**示例 2：**
            **输入：** nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3    **输出：** 10    **解释：** [0,0,1,1, **1** , **1** ,1,1,1, **1** ,1,1,0,0,0,1,1,1,1]    粗体数字从 0 翻转到 1，最长的子数组长度为 10。



**提示：**

  * `1 <= nums.length <= 105`
  * `nums[i]` 不是 `0` 就是 `1`
  * `0 <= k <= nums.length`


**Tags:** Array, Binary Search, Prefix Sum, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/max-consecutive-ones-iii
