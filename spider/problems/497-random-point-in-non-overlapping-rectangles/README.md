# [Random Point in Non-overlapping Rectangles][title]

## Description

给定一个由非重叠的轴对齐矩形的数组 `rects` ，其中 `rects[i] = [ai, bi, xi, yi]` 表示 `(ai, bi)` 是第
`i` 个矩形的左下角点，`(xi, yi)` 是第 `i`
个矩形的右上角角点。设计一个算法来挑选一个随机整数点内的空间所覆盖的一个给定的矩形。矩形周长上的一个点包含在矩形覆盖的空间中。

在一个给定的矩形覆盖的空间内任何整数点都有可能被返回。

**请注意  **，整数点是具有整数坐标的点。

实现 `Solution` 类:

  * `Solution(int[][] rects)` 用给定的矩形数组 `rects` 初始化对象。
  * `int[] pick()` 返回一个随机的整数点 `[u, v]` 在给定的矩形所覆盖的空间内。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg)
            **输入:** ["Solution","pick","pick","pick","pick","pick"]    [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]    **输出:** [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]        **解释：**    Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);    solution.pick(); // 返回 [1, -2]    solution.pick(); // 返回 [1, -1]    solution.pick(); // 返回 [-1, -2]    solution.pick(); // 返回 [-2, -2]    solution.pick(); // 返回 [0, 0]



**提示：**

  * `1 <= rects.length <= 100`
  * `rects[i].length == 4`
  * `-109 <= ai < xi <= 109`
  * `-109 <= bi < yi <= 109`
  * `xi - ai <= 2000`
  * `yi - bi <= 2000`
  * 所有的矩形不重叠。
  * `pick` 最多被调用 `104` 次。




**Tags:** Reservoir Sampling, Math, Binary Search, Ordered Set, Prefix Sum, Randomized

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles
