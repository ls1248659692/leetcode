# [Projection Area of 3D Shapes][title]

## Description

在 `n x n` 的网格 `grid` 中，我们放置了一些与 x，y，z 三轴对齐的 `1 x 1 x 1` 立方体。

每个值 `v = grid[i][j]` 表示 `v` 个正方体叠放在单元格 `(i, j)` 上。

现在，我们查看这些立方体在 `xy` 、`yz` 和 `zx` 平面上的 _投影_ 。

**投影**  就像影子，将 **三维** 形体映射到一个 **二维** 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回 _所有三个投影的总面积_ 。



**示例 1：**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png)
            **输入：** [[1,2],[3,4]]    **输出：** 17    **解释：** 这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。    

**示例  2:**
            **输入：** grid = [[2]]    **输出：** 5    

**示例 3：**
            **输入：** [[1,0],[0,2]]    **输出：** 8    



**提示：**

  * `n == grid.length == grid[i].length`
  * `1 <= n <= 50`
  * `0 <= grid[i][j] <= 50`


**Tags:** Geometry, Array, Math, Matrix

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        g,n,m = grid,len(grid),len(grid[0])
        rmx = sum(max(r) for r in g)
        cmx = sum(max([g[r][c] for r in range(n)]) for c in range(m))
        sm = sum(1 if g[r][c] else 0 for r in range(n)  for c in range(m))
        return rmx+cmx+sm
```

[title]: https://leetcode-cn.com/problems/projection-area-of-3d-shapes
