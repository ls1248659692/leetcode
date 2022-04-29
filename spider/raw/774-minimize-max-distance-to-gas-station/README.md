# [Minimize Max Distance to Gas Station][title]

## Description

整数数组 `stations` 表示 **水平数轴** 上各个加油站的位置。给你一个整数 `k` 。

请你在数轴上增设 `k` 个加油站，新增加油站可以位于 **水平数轴** 上的任意位置，而不必放在整数位置上。

设 `penalty()` 是：增设 `k` 个新加油站后， **相邻** 两个加油站间的最大距离。

请你返回 `penalty()` **** 可能的最小值。与实际答案误差在 `10-6` 范围内的答案将被视作正确答案。

**示例 1：**
            **输入：** stations = [1,2,3,4,5,6,7,8,9,10], k = 9    **输出：** 0.50000    

**示例 2：**
            **输入：** stations = [23,24,36,39,46,56,57,65,84,98], k = 1    **输出：** 14.00000    

**提示：**

  * `10 <= stations.length <= 2000`
  * `0 <= stations[i] <= 108`
  * `stations` 按 **严格递增** 顺序排列
  * `1 <= k <= 106`


**Tags:** Array, Binary Search

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station
