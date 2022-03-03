# [Largest Plus Sign][title]

## Description

在一个 `n x n` 的矩阵 `grid` 中，除了在数组 `mines` 中给出的元素为 `0`，其他每个元素都为 `1`。`mines[i] =
[xi, yi]`表示 `grid[xi][yi] == 0`

返回 _ _`grid` _中包含  `1` 的最大的 **轴对齐** 加号标志的阶数_ 。如果未找到加号标志，则返回 `0` 。

一个 `k` 阶由  _`1`_  组成的 **“轴对称”加号标志** 具有中心网格 `grid[r][c] == 1`
，以及4个从中心向上、向下、向左、向右延伸，长度为 `k-1`，由 `1` 组成的臂。注意，只有加号标志的所有网格要求为 `1` ，别的网格可能为 `0`
也可能为 `1` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg)
            **输入:** n = 5, mines = [[4, 2]]    **输出:** 2    **解释:** 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/06/13/plus2-grid.jpg)
            **输入:** n = 1, mines = [[0, 0]]    **输出:** 0    **解释:** 没有加号标志，返回 0 。    



**提示：**

  * `1 <= n <= 500`
  * `1 <= mines.length <= 5000`
  * `0 <= xi, yi < n`
  * 每一对 `(xi, yi)` 都 **不重复** ​​​​​​​


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/largest-plus-sign
