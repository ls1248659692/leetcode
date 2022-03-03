# [Range Addition II][title]

## Description

给你一个 `m x n` 的矩阵 `M` ** ** ，初始化时所有的 `0` 和一个操作数组 `op` ，其中 `ops[i] = [ai, bi]`
意味着当所有的 `0 <= x < ai` 和 `0 <= y < bi` 时， `M[x][y]` 应该加 1。

在  _执行完所有操作后_  ，计算并返回  _矩阵中最大整数的个数_  。



**示例 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg)
            **输入:** m = 3, n = 3，ops = [[2,2],[3,3]]    **输出:** 4    **解释:** M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。    

**示例 2:**
            **输入:** m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]    **输出:** 4    

**示例 3:**
            **输入:** m = 3, n = 3, ops = []    **输出:** 9    



**提示:**

  * `1 <= m, n <= 4 * 104`
  * `0 <= ops.length <= 104`
  * `ops[i].length == 2`
  * `1 <= ai <= m`
  * `1 <= bi <= n`


**Tags:** Array, Math

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/range-addition-ii
