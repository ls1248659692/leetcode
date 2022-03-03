# [3Sum With Multiplicity][title]

## Description

给定一个整数数组 `arr` ，以及一个整数 `target` 作为目标值，返回满足 `i < j < k` 且 `arr[i] + arr[j] +
arr[k] == target` 的元组 `i, j, k` 的数量。

由于结果会非常大，请返回 `109 + 7` 的模。



**示例 1：**
            **输入：** arr = [1,1,2,2,3,3,4,4,5,5], target = 8    **输出：** 20    **解释：**    按值枚举(arr[i], arr[j], arr[k])：    (1, 2, 5) 出现 8 次；    (1, 3, 4) 出现 8 次；    (2, 2, 4) 出现 2 次；    (2, 3, 3) 出现 2 次。    

**示例 2：**
            **输入：** arr = [1,1,2,2,2,2], target = 5    **输出：** 12    **解释：**    arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：    我们从 [1,1] 中选择一个 1，有 2 种情况，    从 [2,2,2,2] 中选出两个 2，有 6 种情况。    



**提示：**

  * `3 <= arr.length <= 3000`
  * `0 <= arr[i] <= 100`
  * `0 <= target <= 300`


**Tags:** Array, Hash Table, Two Pointers, Counting, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/3sum-with-multiplicity
