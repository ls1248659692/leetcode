# [Maximum Subarray Sum After One Operation][title]

## Description

你有一个整数数组 `nums`。你只能将一个元素 `nums[i]` 替换为 `nums[i] * nums[i]`。

返回替换后的最大子数组和。

**示例 1：**
            **输入：** nums = [2,-1,-4,-3]    **输出：** 17    **解释：** 你可以把-4替换为16(-4*(-4))，使nums = [2,-1, **16** ,-3]. 现在，最大子数组和为 2 + -1 + 16 = 17.

**示例 2：**
            **输入：** nums = [1,-1,1,1,-1,-1,1]    **输出：** 4    **解释：** 你可以把第一个-1替换为1，使 nums = [1, **1** ,1,1,-1,-1,1]. 现在，最大子数组和为 1 + 1 + 1 + 1 = 4.

**提示：**

  * `1 <= nums.length <= 105`
  * `-104 <= nums[i] <= 104`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-subarray-sum-after-one-operation
