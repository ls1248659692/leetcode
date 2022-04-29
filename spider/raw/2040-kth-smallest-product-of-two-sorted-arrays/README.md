# [Kth Smallest Product of Two Sorted Arrays][title]

## Description

给你两个 **从小到大排好序**  且下标从 **0**  开始的整数数组 `nums1` 和 `nums2` 以及一个整数 `k` ，请你返回第 _
_`k` （从 **1**  开始编号）小的 `nums1[i] * nums2[j]` _ _ 的乘积，其中 _ _`0 <= i <
nums1.length` __ 且 __`0 <= j < nums2.length` 。



**示例 1：**
            **输入：** nums1 = [2,5], nums2 = [3,4], k = 2    **输出：** 8    **解释：** 第 2 小的乘积计算如下：    - nums1[0] * nums2[0] = 2 * 3 = 6    - nums1[0] * nums2[1] = 2 * 4 = 8    第 2 小的乘积为 8 。    

**示例 2：**
            **输入：** nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6    **输出：** 0    **解释：** 第 6 小的乘积计算如下：    - nums1[0] * nums2[1] = (-4) * 4 = -16    - nums1[0] * nums2[0] = (-4) * 2 = -8    - nums1[1] * nums2[1] = (-2) * 4 = -8    - nums1[1] * nums2[0] = (-2) * 2 = -4    - nums1[2] * nums2[0] = 0 * 2 = 0    - nums1[2] * nums2[1] = 0 * 4 = 0    第 6 小的乘积为 0 。    

**示例 3：**
            **输入：** nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3    **输出：** -6    **解释：** 第 3 小的乘积计算如下：    - nums1[0] * nums2[4] = (-2) * 5 = -10    - nums1[0] * nums2[3] = (-2) * 4 = -8    - nums1[4] * nums2[0] = 2 * (-3) = -6    第 3 小的乘积为 -6 。    



**提示：**

  * `1 <= nums1.length, nums2.length <= 5 * 104`
  * `-105 <= nums1[i], nums2[j] <= 105`
  * `1 <= k <= nums1.length * nums2.length`
  * `nums1` 和 `nums2` 都是从小到大排好序的。


**Tags:** Array, Binary Search

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/kth-smallest-product-of-two-sorted-arrays
