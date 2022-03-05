# [Shift 2D Grid][title]

## Description

给你一个 `m` 行 `n` 列的二维网格 `grid` 和一个整数 `k`。你需要将 `grid` 迁移 `k` 次。

每次「迁移」操作将会引发下述活动：

  * 位于 `grid[i][j]` 的元素将会移动到 `grid[i][j + 1]`。
  * 位于 `grid[i][n - 1]` 的元素将会移动到 `grid[i + 1][0]`。
  * 位于 `grid[m - 1][n - 1]` 的元素将会移动到 `grid[0][0]`。

请你返回 `k` 次迁移操作后最终得到的 **二维网格** 。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/16/e1-1.png)
            **输入：** grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1    **输出：** [[9,1,2],[3,4,5],[6,7,8]]    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/16/e2-1.png)
            **输入：** grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4    **输出：** [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]    

**示例 3：**
            **输入：** grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9    **输出：** [[1,2,3],[4,5,6],[7,8,9]]    

**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m <= 50`
  * `1 <= n <= 50`
  * `-1000 <= grid[i][j] <= 1000`
  * `0 <= k <= 100`


**Tags:** Array, Matrix, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ele = []
        for x in grid:
            for y in x:
                ele.append(y)
        k = k % len(ele)
        ele = ele[-k:] + ele[:-k]
        print(ele)
        i = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                grid[a][b] = ele[i]
                i = i +1
        return(grid)
```

[title]: https://leetcode-cn.com/problems/shift-2d-grid
