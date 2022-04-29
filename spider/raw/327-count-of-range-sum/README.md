# [Count of Range Sum][title]

## Description

给你一个整数数组 `nums` 以及两个整数 `lower` 和 `upper` 。求数组中，值位于范围 `[lower, upper]` （包含
`lower` 和 `upper`）之内的 **区间和的个数** 。

**区间和** `S(i, j)` 表示在 `nums` 中，位置从 `i` 到 `j` 的元素之和，包含 `i` 和 `j` (`i` ≤ `j`)。

**示例 1：**
            **输入：** nums = [-2,5,-1], lower = -2, upper = 2    **输出：** 3    **解释：** 存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。    

**示例 2：**
            **输入：** nums = [0], lower = 0, upper = 0    **输出：** 1    

**提示：**

  * `1 <= nums.length <= 105`
  * `-231 <= nums[i] <= 231 - 1`
  * `-105 <= lower <= upper <= 105`
  * 题目数据保证答案是一个 **32 位** 的整数


**Tags:** Binary Indexed Tree, Segment Tree, Array, Binary Search, Divide and Conquer, Ordered Set, Merge Sort

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/count-of-range-sum
