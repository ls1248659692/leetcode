# [Missing Number In Arithmetic Progression][title]

## Description

在某个数组 `arr` 中，值符合等差数列的数值规律：在 `0 <= i < arr.length - 1` 的前提下，`arr[i+1] -
arr[i]` 的值都相等。

我们会从该数组中删除一个 **既不是第一个** 也 **  不是最后一个的值**，得到一个新的数组  `arr`。

给你这个缺值的数组 `arr`，返回 _被删除的那个数_ 。



**示例 1：**
            **输入：** arr = [5,7,11,13]    **输出：** 9    **解释：** 原来的数组是 [5,7, **9** ,11,13]。    

**示例 2：**
            **输入：** arr = [15,13,12]    **输出：** 14    **解释：** 原来的数组是 [15, **14** ,13,12]。



**提示：**

  * `3 <= arr.length <= 1000`
  * `0 <= arr[i] <= 105`
  * 给定的数组 **保证** 是一个有效的数组。


**Tags:** Array, Math

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/missing-number-in-arithmetic-progression
