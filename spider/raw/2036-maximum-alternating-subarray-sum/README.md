# [Maximum Alternating Subarray Sum][title]

## Description

**子数组** 是以 **0** 下标开始的数组的连续非空子序列，从 `i` 到 `j`（`0 <= i <= j < nums.length`）的
**子数组交替和** 被定义为 `nums[i] - nums[i+1] + nums[i+2] - ... +/- nums[j]` 。

给定一个以 **0** 下标开始的整数数组`nums`，返回它所有可能的交替子数组和的最大值。



**示例 1：**
            **输入：** nums = [3,-1,1,2]    **输出：** 5    **解释：**    子数组 [3,-1,1]有最大的交替子数组和3 - (-1) + 1 = 5.    

**示例 2：**
            **输入：** nums = [2,2,2,2,2]    **输出：** 2    **解释：**    子数组 [2], [2,2,2]和 [2,2,2,2,2]有相同的最大交替子数组和为2    [2]: 2.    [2,2,2]: 2 - 2 + 2 = 2.    [2,2,2,2,2]: 2 - 2 + 2 - 2 + 2 = 2.    

**示例 3：**
            **输入：** nums = [1]    **输出：** 1    **解释：**    仅有一个非空子数组，为 [1]，它的交替子数组和为 1    



**提示：**

  * `1 <= nums.length <= 105`
  * `-105 <= nums[i] <= 105`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-alternating-subarray-sum
