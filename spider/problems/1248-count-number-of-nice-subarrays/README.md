# [Count Number of Nice Subarrays][title]

## Description

给你一个整数数组 `nums` 和一个整数 `k`。如果某个连续子数组中恰好有 `k` 个奇数数字，我们就认为这个子数组是「 **优美子数组** 」。

请返回这个数组中 **「优美子数组」** 的数目。



**示例 1：**
            **输入：** nums = [1,1,2,1,1], k = 3    **输出：** 2    **解释：** 包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。    

**示例 2：**
            **输入：** nums = [2,4,6], k = 1    **输出：** 0    **解释：** 数列中不包含任何奇数，所以不存在优美子数组。    

**示例 3：**
            **输入：** nums = [2,2,2,1,2,2,1,2,2,2], k = 2    **输出：** 16    



**提示：**

  * `1 <= nums.length <= 50000`
  * `1 <= nums[i] <= 10^5`
  * `1 <= k <= nums.length`


**Tags:** Array, Hash Table, Math, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/count-number-of-nice-subarrays
