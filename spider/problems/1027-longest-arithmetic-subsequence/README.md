# [Longest Arithmetic Subsequence][title]

## Description

给你一个整数数组 `nums`，返回 `nums` 中最长等差子序列的 **长度** 。

回想一下，`nums` 的子序列是一个列表 `nums[i1], nums[i2], ..., nums[ik]` ，且 `0 <= i1 < i2 <
... < ik <= nums.length - 1`。并且如果 `seq[i+1] - seq[i]`( `0 <= i < seq.length -
1`) 的值都相同，那么序列 `seq` 是等差的。



**示例 1：**
            **输入：** nums = [3,6,9,12]    **输出：** 4    **解释：**    整个数组是公差为 3 的等差数列。    

**示例 2：**
            **输入：** nums = [9,4,7,2,10]    **输出：** 3    **解释：**    最长的等差子序列是 [4,7,10]。    

**示例 3：**
            **输入：** nums = [20,1,15,3,10,5,8]    **输出：** 4    **解释：**    最长的等差子序列是 [20,15,10,5]。    



**提示：**

  * `2 <= nums.length <= 1000`
  * `0 <= nums[i] <= 500`


**Tags:** Array, Hash Table, Binary Search, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/longest-arithmetic-subsequence
