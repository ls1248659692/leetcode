# [Advantage Shuffle][title]

## Description

给定两个大小相等的数组 `A` 和 `B`，A 相对于 B 的 _优势_ 可以用满足 `A[i] > B[i]` 的索引 `i` 的数目来描述。

返回 `A` 的 **任意** 排列，使其相对于 `B` 的优势最大化。



**示例 1：**
            **输入：** A = [2,7,11,15], B = [1,10,4,11]    **输出：** [2,11,7,15]    

**示例 2：**
            **输入：** A = [12,24,8,32], B = [13,25,32,11]    **输出：** [24,32,8,12]    



**提示：**

  1. `1 <= A.length = B.length <= 10000`
  2. `0 <= A[i] <= 10^9`
  3. `0 <= B[i] <= 10^9`


**Tags:** Greedy, Array, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/advantage-shuffle
