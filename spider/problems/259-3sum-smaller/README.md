# [3Sum Smaller][title]

## Description

给定一个长度为 `n` 的整数数组和一个目标值 `target` ，寻找能够使条件 `nums[i] + nums[j] + nums[k] <
target` 成立的三元组  `i, j, k` 个数（`0 <= i < j < k < n`）。



**示例 1：**
            **输入:** _nums_ = [-2,0,1,3], _target_ = 2    **输出:** 2     **解释:** 因为一共有两个三元组满足累加和小于 2:         [-2,0,1]         [-2,0,3]    

**示例 2：**
            **输入:** _nums_ = [], _target_ = 0    **输出:** 0 

**示例 3：**
            **输入:** _nums_ = [0], _target_ = 0    **输出:** 0 



**提示:**

  * `n == nums.length`
  * `0 <= n <= 3500`
  * `-100 <= nums[i] <= 100`
  * `-100 <= target <= 100`


**Tags:** Array, Two Pointers, Binary Search, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/3sum-smaller
