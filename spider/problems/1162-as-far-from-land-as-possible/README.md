# [As Far from Land as Possible][title]

## Description

你现在手里有一份大小为 `n x n` 的 网格 `grid`，上面的每个 单元格 都用 `0` 和 `1` 标记好了。其中 `0` 代表海洋，`1`
代表陆地。

请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。如果网格上只有陆地或者海洋，请返回 `-1`。

我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：`(x0, y0)` 和 `(x1, y1)` 这两个单元格之间的距离是
`|x0 - x1| + |y0 - y1|` 。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/08/17/1336_ex1.jpeg)**
            **输入：** grid = [[1,0,1],[0,0,0],[1,0,1]]    **输出：** 2    **解释：**    海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/08/17/1336_ex2.jpeg)**
            **输入：** grid = [[1,0,0],[0,0,0],[0,0,0]]    **输出：** 4    **解释：**    海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。    



**提示：**

  * `n == grid.length`
  * `n == grid[i].length`
  * `1 <= n <= 100`
  * `grid[i][j]` 不是 `0` 就是 `1`


**Tags:** Breadth-First Search, Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def max_link(r,c,hset):
            h= g[r][c]
            for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:      
                rr,cc,h1= r+i,c+j,h+1          
                if 0<=rr<m and 0<=cc<n and  h1<g[rr][cc]:
                    g[rr][cc]=h1
                    hset.add((rr,cc))

        g,m,n= grid,len(grid),len(grid[0])
        if sum(sum(r) for r in g) in [0,n*m]:return -1
        m_n= m*n
        g = [ [0 if g[i][j]==1 else m_n for j in range(n)] for i in range(m)]
        hset = [(i,j) for i in range(m) for j in range(n) if g[i][j]==0]
        for h in range(0,m_n+1):
            _hset,hset=set(hset),set()
            for r,c in _hset:
                max_link(r,c,hset)
        return max(max(r) for r in g)
```

[title]: https://leetcode-cn.com/problems/as-far-from-land-as-possible
