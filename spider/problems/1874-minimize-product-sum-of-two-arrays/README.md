# [Minimize Product Sum of Two Arrays][title]

## Description

给定两个 **长度相等** 的数组`a`和`b`，它们的 **乘积和** 为数组中所有的`a[i] * b[i]`之和，其中`0 <= i <
a.length`。

  * 比如`a = [1,2,3,4]`，`b = [5,2,3,1]`时，它们的 **乘积和** 为`1*5 + 2*2 + 3*3 + 4*1 = 22`

现有两个长度都为`n`的数组`nums1`和`nums2`，你可以以 **任意顺序排序**`nums1`，请返回它们的 **最小乘积和** 。

**示例 1:**
            **输入:** nums1 = [5,3,4,2], nums2 = [4,2,2,5]    **输出:** 40    **解释:** 将 num1 重新排列为 [3,5,4,2] 后，可由 **** [3,5,4,2] 和 [4,2,2,5] 得到最小乘积和 3*4 + 5*2 + 4*2 + 2*5 = 40。    

**示例 2:**
            **输入:** nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]    **输出:** 65    **解释:** 将 num1 重新排列为 [5,7,4,1,2] 后，可由 **** [5,7,4,1,2] 和 [3,2,4,8,6] 得到最小乘积和 5*3 + 7*2 + 4*4 + 1*8 + 2*6 = 65。    

**提示:**

  * `n == nums1.length == nums2.length`
  * `1 <= n <= 105`
  * `1 <= nums1[i], nums2[i] <= 100`


**Tags:** Greedy, Array, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimize-product-sum-of-two-arrays
