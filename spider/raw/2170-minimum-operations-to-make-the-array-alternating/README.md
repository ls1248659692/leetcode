# [Minimum Operations to Make the Array Alternating][title]

## Description

给你一个下标从 **0** 开始的数组 `nums` ，该数组由 `n` 个正整数组成。

如果满足下述条件，则数组 `nums` 是一个 **交替数组** ：

  * `nums[i - 2] == nums[i]` ，其中 `2 <= i <= n - 1` 。
  * `nums[i - 1] != nums[i]` ，其中 `1 <= i <= n - 1` 。

在一步 **操作** 中，你可以选择下标 `i` 并将 `nums[i]` **更改** 为 **任一** 正整数。

返回使数组变成交替数组的 **最少操作数** 。



**示例 1：**
            **输入：** nums = [3,1,3,2,4,3]    **输出：** 3    **解释：**    使数组变成交替数组的方法之一是将该数组转换为 [3,1,3, _ **1**_ , _ **3**_ , _ **1**_ ] 。    在这种情况下，操作数为 3 。    可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。

**示例 2：**
            **输入：** nums = [1,2,2,2,2]    **输出：** 2    **解释：**    使数组变成交替数组的方法之一是将该数组转换为 [1,2, _ **1**_ ,2, _ **1**_ ].    在这种情况下，操作数为 2 。    注意，数组不能转换成 [ _ **2**_ ,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。    



**提示：**

  * `1 <= nums.length <= 105`
  * `1 <= nums[i] <= 105`


**Tags:** Greedy, Array, Hash Table, Counting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-alternating
