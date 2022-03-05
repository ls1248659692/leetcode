# [最小路径之和][title]

## Description

给定一个包含非负整数的 `_m_  x  _n_` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明：** 一个机器人每次只能向下或者向右移动一步。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)
            **输入：** grid = [[1,3,1],[1,5,1],[4,2,1]]    **输出：** 7    **解释：** 因为路径 1->3->1->1->1 的总和最小。    

**示例 2：**
            **输入：** grid = [[1,2,3],[4,5,6]]    **输出：** 12    



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m, n <= 200`
  * `0 <= grid[i][j] <= 100`



注意：本题与主站 64 题相同： <https://leetcode-cn.com/problems/minimum-path-sum/>


**Tags:** Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g,n,m = grid,len(grid),len(grid[0])
        zskip = lambda i,j,x: 99999 if not 0<=i<n or not 0<=j<m else x
        f=[[g[0][0]]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:continue
                f[i][j]= min(zskip(i,j-1,f[i][j-1]),zskip(i-1,j,f[i-1][j]))+g[i][j]
        return f[-1][-1]        
```

[title]: https://leetcode-cn.com/problems/0i0mDW
