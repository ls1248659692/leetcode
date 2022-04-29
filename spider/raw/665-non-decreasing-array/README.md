# [Non-decreasing Array][title]

## Description

给你一个长度为 `n` 的整数数组 `nums` ，请你判断在 **最多** 改变 `1` 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 `i` `(0 <= i <= n-2)`，总满足 `nums[i] <= nums[i + 1]`。



**示例 1:**
            **输入:** nums = [4,2,3]    **输出:** true    **解释:** 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。    

**示例 2:**
            **输入:** nums = [4,2,1]    **输出:** false    **解释:** 你不能在只改变一个元素的情况下将其变为非递减数列。    



**提示：**

  * `n == nums.length`
  * `1 <= n <= 104`
  * `-105 <= nums[i] <= 105`


**Tags:** Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/non-decreasing-array
