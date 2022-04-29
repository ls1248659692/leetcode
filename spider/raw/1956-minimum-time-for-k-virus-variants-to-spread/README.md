# [Minimum Time For K Virus Variants to Spread][title]

## Description

在无限大的二维平面上有 `n` 种 **不同** 的病毒。给定二维数组 `points` ，第 `i` 项 `points[i] = [xi, yi]`
说明第 `0` 天有一种病毒在点 `(xi, yi)` 。注意初始状态下，可能有 **多种** 病毒在 **同一点** 上。

每天，被感染的点会把它感染的病毒传播到上、下、左、右四个邻居点。

现给定一个整数 `k` ，问 **最少** 需要多少天，方能找到一点感染 **至少** `k` 种病毒？



**示例 1：**

**![](https://assets.leetcode.com/uploads/2021/06/30/case-1.png)**
            **输入：** points = [[1,1],[6,1]], k = 2    **输出：** 3    **解释：** 在第 3 天，点 (3,1) 与 (4,1) 将感染所有 2 种病毒。    

**示例 2：**

**![](https://assets.leetcode.com/uploads/2021/06/30/case-2.png)**
            **输入：** points = [[3,3],[1,2],[9,2]], k = 2    **输出：** 2    **解释：** 在第 2 天, 点 (1,2), (1,3), (2,1), (2,2), (3,1) 和 (3,3) 将会感染前两种病毒。    

**示例 3：**

**![](https://assets.leetcode.com/uploads/2021/06/30/case-2.png)**
            **输入：** points = [[3,3],[1,2],[9,2]], k = 3    **输出：** 4    **解释：** 在第 4 天，点 (5,2) 会感染所有 3 种病毒。    



**提示：**

  * `n == points.length`
  * `2 <= n <= 50`
  * `points[i].length == 2`
  * `1 <= xi, yi <= 109`
  * `2 <= k <= n`


**Tags:** Geometry, Array, Math, Binary Search, Enumeration

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-time-for-k-virus-variants-to-spread
