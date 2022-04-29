# [Maximum Number of Non-Overlapping Subarrays With Sum Equals Target][title]

## Description

给你一个数组 `nums` 和一个整数 `target` 。

请你返回  **非空不重叠**  子数组的最大数目，且每个子数组中数字和都为 `target` 。



**示例 1：**
            **输入：** nums = [1,1,1,1,1], target = 2    **输出：** 2    **解释：** 总共有 2 个不重叠子数组（加粗数字表示） [ **1,1** ,1, **1,1** ] ，它们的和为目标值 2 。    

**示例 2：**
            **输入：** nums = [-1,3,5,1,4,2,-9], target = 6    **输出：** 2    **解释：** 总共有 3 个子数组和为 6 。    ([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。

**示例 3：**
            **输入：** nums = [-2,6,6,3,5,4,1,2,8], target = 10    **输出：** 3    

**示例 4：**
            **输入：** nums = [0,0,0], target = 0    **输出：** 3    



**提示：**

  * `1 <= nums.length <= 10^5`
  * `-10^4 <= nums[i] <= 10^4`
  * `0 <= target <= 10^6`


**Tags:** Greedy, Array, Hash Table, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target
