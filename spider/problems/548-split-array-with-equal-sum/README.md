# [Split Array with Equal Sum][title]

## Description

给定一个有 `n` 个整数的数组 `nums` ，如果能找到满足以下条件的三元组  `(i, j, k)`  则返回 `true` ：

  1. `0 < i, i + 1 < j, j + 1 < k < n - 1`
  2. 子数组 `(0, i - 1)` ， `(i + 1, j - 1)` ， `(j + 1, k - 1)` ， `(k + 1, n - 1)` 的和应该相等。

这里我们定义子数组 `(l, r)` 表示原数组从索引为 `l` 的元素开始至索引为 `r` 的元素。



**示例 1:  **
            **输入:** nums = [1,2,1,2,1,2,1]    **输出:** True    **解释:**    i = 1, j = 3, k = 5.     sum(0, i - 1) = sum(0, 0) = 1    sum(i + 1, j - 1) = sum(2, 2) = 1    sum(j + 1, k - 1) = sum(4, 4) = 1    sum(k + 1, n - 1) = sum(6, 6) = 1    

**示例 2:**
            **输入:** nums = [1,2,1,2,1,2,1,2]    **输出:** false    



**提示:**

  * `n == nums.length`
  * `1 <= n <= 2000`
  * `-106 <= nums[i] <= 106`


**Tags:** Array, Prefix Sum

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/split-array-with-equal-sum
