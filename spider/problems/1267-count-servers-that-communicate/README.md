# [Count Servers that Communicate][title]

## Description

这里有一幅服务器分布图，服务器的位置标识在 `m * n` 的整数矩阵网格 `grid` 中，1 表示单元格上有服务器，0 表示没有。

如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。

请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/24/untitled-diagram-6.jpg)
            **输入：** grid = [[1,0],[0,1]]    **输出：** 0    **解释：** 没有一台服务器能与其他服务器进行通信。

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/24/untitled-diagram-4-1.jpg)**
            **输入：** grid = [[1,0],[1,1]]    **输出：** 3    **解释：** 所有这些服务器都至少可以与一台别的服务器进行通信。    

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/24/untitled-diagram-1-3.jpg)
            **输入：** grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]    **输出：** 4    **解释：** 第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。    



**提示：**

  * `m == grid.length`
  * `n == grid[i].length`
  * `1 <= m <= 250`
  * `1 <= n <= 250`
  * `grid[i][j] == 0 or 1`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Counting, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cnt,g,m,n,gt = 0,grid,len(grid),len(grid[0]),list(zip(*grid))
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    if g[i].count(1) + gt[j].count(1) > 2:
                        cnt += 1
        return cnt
```

[title]: https://leetcode-cn.com/problems/count-servers-that-communicate
