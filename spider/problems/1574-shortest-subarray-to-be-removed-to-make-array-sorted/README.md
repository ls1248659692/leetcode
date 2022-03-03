# [Shortest Subarray to be Removed to Make Array Sorted][title]

## Description

给你一个整数数组 `arr` ，请你删除一个子数组（可以为空），使得 `arr` 中剩下的元素是 **非递减** 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。



**示例 1：**
            **输入：** arr = [1,2,3,10,4,2,3,5]    **输出：** 3    **解释：** 我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。    另一个正确的解为删除子数组 [3,10,4] 。

**示例 2：**
            **输入：** arr = [5,4,3,2,1]    **输出：** 4    **解释：** 由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。    

**示例 3：**
            **输入：** arr = [1,2,3]    **输出：** 0    **解释：** 数组已经是非递减的了，我们不需要删除任何元素。    

**示例 4：**
            **输入：** arr = [1]    **输出：** 0    



**提示：**

  * `1 <= arr.length <= 10^5`
  * `0 <= arr[i] <= 10^9`


**Tags:** Stack, Array, Two Pointers, Binary Search, Monotonic Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted
