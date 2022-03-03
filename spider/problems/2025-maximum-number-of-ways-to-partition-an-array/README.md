# [Maximum Number of Ways to Partition an Array][title]

## Description

给你一个下标从 **0**  开始且长度为 `n` 的整数数组 `nums` 。 **分割**  数组 `nums` 的方案数定义为符合以下两个条件的
`pivot` 数目：

  * `1 <= pivot < n`
  * `nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]`

同时给你一个整数 `k` 。你可以将 `nums` 中  **一个**  元素变为 `k` 或  **不改变**  数组。

请你返回在 **至多**  改变一个元素的前提下， **最多**  有多少种方法 **分割**  `nums` 使得上述两个条件都满足。



**示例 1：**
            **输入：** nums = [2,-1,2], k = 3    **输出：** 1    **解释：** 一个最优的方案是将 nums[0] 改为 k 。数组变为 [ _ **3**_ ,-1,2] 。    有一种方法分割数组：    - pivot = 2 ，我们有分割 [3,-1 | 2]：3 + -1 == 2 。    

**示例 2：**
            **输入：** nums = [0,0,0], k = 1    **输出：** 2    **解释：** 一个最优的方案是不改动数组。    有两种方法分割数组：    - pivot = 1 ，我们有分割 [0 | 0,0]：0 == 0 + 0 。    - pivot = 2 ，我们有分割 [0,0 | 0]: 0 + 0 == 0 。    

**示例 3：**
            **输入：** nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33    **输出：** 4    **解释：** 一个最优的方案是将 nums[2] 改为 k 。数组变为 [22,4, _ **-33**_ ,-20,-15,15,-16,7,19,-10,0,-13,-14] 。    有四种方法分割数组。    



**提示：**

  * `n == nums.length`
  * `2 <= n <= 105`
  * `-105 <= k, nums[i] <= 105`


**Tags:** Array, Hash Table, Counting, Enumeration, Prefix Sum

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/maximum-number-of-ways-to-partition-an-array
