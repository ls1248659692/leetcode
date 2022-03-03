# [Partition Array Into Two Arrays to Minimize Sum Difference][title]

## Description

给你一个长度为 `2 * n` 的整数数组。你需要将 `nums` 分成  **两个**  长度为 `n` 的数组，分别求出两个数组的和，并 **最小化**
两个数组和之  **差的绝对值**  。`nums` 中每个元素都需要放入两个数组之一。

请你返回  **最小**  的数组和之差。



**示例 1：**

![example-1](https://assets.leetcode.com/uploads/2021/10/02/ex1.png)
            **输入：** nums = [3,9,7,3]    **输出：** 2    **解释：** 最优分组方案是分成 [3,9] 和 [7,3] 。    数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。    

**示例 2：**
            **输入：** nums = [-36,36]    **输出：** 72    **解释：** 最优分组方案是分成 [-36] 和 [36] 。    数组和之差的绝对值为 abs((-36) - (36)) = 72 。    

**示例 3：**

![example-3](https://assets.leetcode.com/uploads/2021/10/02/ex3.png)
            **输入：** nums = [2,-1,0,4,-2,-9]    **输出：** 0    **解释：** 最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。    数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。    



**提示：**

  * `1 <= n <= 15`
  * `nums.length == 2 * n`
  * `-107 <= nums[i] <= 107`


**Tags:** Bit Manipulation, Array, Two Pointers, Binary Search, Dynamic Programming, Bitmask, Ordered Set

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference
