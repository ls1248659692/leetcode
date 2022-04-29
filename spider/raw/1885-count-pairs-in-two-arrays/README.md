# [Count Pairs in Two Arrays][title]

## Description

给你两个长度为 `n` 的整数数组 `nums1` 和 `nums2` ，找出所有满足 `i < j` 且 `nums1[i] + nums1[j] >
nums2[i] + nums2[j]` 的数对 `(i, j)` 。

返回满足条件数对的 **个数** 。



**示例 1：**
            **输入：** nums1 = [2,1,2,1], nums2 = [1,2,1,2]    **输出：** 1    **解释：** 满足条件的数对有 1 个：(0, 2) ，因为 nums1[0] + nums1[2] = 2 + 2 > nums2[0] + nums2[2] = 1 + 1

**示例 2：**
            **输入：** nums1 = [1,10,6,2], nums2 = [1,4,1,5]    **输出：** 5    **解释：** 以下数对满足条件：    - (0, 1) 因为 nums1[0] + nums1[1] = 1 + 10 > nums2[0] + nums2[1] = 1 + 4    - (0, 2) 因为 nums1[0] + nums1[2] = 1 + 6 > nums2[0] + nums2[2] = 1 + 1    - (1, 2) 因为 nums1[1] + nums1[2] = 10 + 6 > nums2[1] + nums2[2] = 4 + 1    - (1, 3) 因为 nums1[1] + nums1[3] = 10 + 2 > nums2[1] + nums2[3] = 4 + 5    - (2, 3) 因为 nums1[2] + nums1[3] = 6 + 2 > nums2[2] + nums2[3] = 1 + 5    



**提示：**

  * `n == nums1.length == nums2.length`
  * `1 <= n <= 105`
  * `1 <= nums1[i], nums2[i] <= 105`


**Tags:** Array, Binary Search, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/count-pairs-in-two-arrays
