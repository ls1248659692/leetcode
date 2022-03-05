# [构建乘积数组 LCOF][title]

## Description

给定一个数组 `A[0,1,…,n-1]`，请构建一个数组 `B[0,1,…,n-1]`，其中 `B[i]` 的值是数组 `A` 中除了下标 `i`
以外的元素的积, 即 `B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]`。不能使用除法。

**示例:**
            **输入:** [1,2,3,4,5]    **输出:** [120,60,40,30,24]

**提示：**

  * 所有元素乘积之和不会溢出 32 位整数
  * `a.length <= 100000`


**Tags:** Array, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
