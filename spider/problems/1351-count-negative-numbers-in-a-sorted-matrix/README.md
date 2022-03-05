# [Count Negative Numbers in a Sorted Matrix][title]

## Description

给你一个 `m * n` 的矩阵 `grid`，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。

请你统计并返回 `grid` 中 **负数** 的数目。

**示例 1：**
            **输入：** grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]    **输出：** 8    **解释：** 矩阵中共有 8 个负数。    

**示例 2：**
            **输入：** grid = [[3,2],[1,0]]    **输出：** 0    

**示例 3：**
            **输入：** grid = [[1,-1],[-1,-1]]    **输出：** 3    

**示例 4：**
            **输入：** grid = [[-1]]    **输出：** 1    

**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 100`
  * `-100 <= grid[i][j] <= 100`

**进阶：** 你可以设计一个时间复杂度为 `O(n + m)` 的解决方案吗？


**Tags:** Array, Binary Search, Matrix

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]<0)
```

[title]: https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix
