# [Number of Subsequences That Satisfy the Given Sum Condition][title]

## Description

给你一个整数数组 `nums` 和一个整数 `target` 。

请你统计并返回 `nums` 中能满足其最小元素与最大元素的 **和** 小于或等于 `target` 的 **非空** 子序列的数目。

由于答案可能很大，请将结果对 10^9 + 7 取余后返回。



**示例 1：**
            **输入：** nums = [3,5,6,7], target = 9    **输出：** 4    **解释：** 有 4 个子序列满足该条件。    [3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)    [3,5] -> (3 + 5 <= 9)    [3,5,6] -> (3 + 6 <= 9)    [3,6] -> (3 + 6 <= 9)    

**示例 2：**
            **输入：** nums = [3,3,6,8], target = 10    **输出：** 6    **解释：** 有 6 个子序列满足该条件。（nums 中可以有重复数字）    [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

**示例 3：**
            **输入：** nums = [2,3,3,4,6,7], target = 12    **输出：** 61    **解释：** 共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）    有效序列总数为（63 - 2 = 61）    

**示例 4：**
            **输入：** nums = [5,2,4,1,7,6,8], target = 16    **输出：** 127    **解释：** 所有非空子序列都满足条件 (2^7 - 1) = 127



**提示：**

  * `1 <= nums.length <= 10^5`
  * `1 <= nums[i] <= 10^6`
  * `1 <= target <= 10^6`


**Tags:** Array, Two Pointers, Binary Search, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition
