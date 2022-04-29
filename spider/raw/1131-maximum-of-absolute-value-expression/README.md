# [Maximum of Absolute Value Expression][title]

## Description

给你两个长度相等的整数数组，返回下面表达式的最大值：

`|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|`

其中下标 `i`，`j` 满足 `0 <= i, j < arr1.length`。



**示例 1：**
            **输入：** arr1 = [1,2,3,4], arr2 = [-1,4,5,6]    **输出：** 13    

**示例 2：**
            **输入：** arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]    **输出：** 20



**提示：**

  * `2 <= arr1.length == arr2.length <= 40000`
  * `-10^6 <= arr1[i], arr2[i] <= 10^6`


**Tags:** Array, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-of-absolute-value-expression
