# [Minimum Swaps To Make Sequences Increasing][title]

## Description

我们有两个长度相等且不为空的整型数组 `nums1` 和 `nums2` 。在一次操作中，我们可以交换 `nums1[i]` 和
`nums2[i]`的元素。

  * 例如，如果 `nums1 = [1,2,3, _8_ ]` ， `nums2 =[5,6,7, _4_ ]` ，你可以交换 `i = 3` 处的元素，得到 `nums1 =[1,2,3,4]` 和 `nums2 =[5,6,7,8]` 。

返回 _使`nums1` 和 `nums2` **严格递增  **所需操作的最小次数_ 。

数组 `arr`  **严格递增** 且  `arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1]` 。

**注意：**

  * 用例保证可以实现操作。



**示例 1:**
            **输入:** nums1 = [1,3,5,4], nums2 = [1,2,3,7]    **输出:** 1    **解释:**    交换 A[3] 和 B[3] 后，两个数组如下:    A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]    两个数组均为严格递增的。

**示例 2:**
            **输入:** nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]    **输出:** 1    



**提示:**

  * `2 <= nums1.length <= 105`
  * `nums2.length == nums1.length`
  * `0 <= nums1[i], nums2[i] <= 2 * 105`


**Tags:** Array, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing
