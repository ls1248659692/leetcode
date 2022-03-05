# [01 Matrix][title]

## Description

给定一个由 `0` 和 `1` 组成的矩阵 `mat` ，请输出一个大小相同的矩阵，其中每一个格子是 `mat` 中对应位置元素到最近的 `0` 的距离。

两个相邻元素间的距离为 `1` 。

**示例 1：**

![](https://pic.leetcode-cn.com/1626667201-NCWmuP-image.png)
            **输入：** mat = **** [[0,0,0],[0,1,0],[0,0,0]]    **输出：** [[0,0,0],[0,1,0],[0,0,0]]    

**示例 2：**

![](https://pic.leetcode-cn.com/1626667205-xFxIeK-image.png)
            **输入：** mat = **** [[0,0,0],[0,1,0],[1,1,1]]    **输出：** [[0,0,0],[0,1,0],[1,2,1]]    

**提示：**

  * `m == mat.length`
  * `n == mat[i].length`
  * `1 <= m, n <= 104`
  * `1 <= m * n <= 104`
  * `mat[i][j] is either 0 or 1.`
  * `mat` 中至少有一个 `0 `


**Tags:** Breadth-First Search, Array, Dynamic Programming, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def max_link(r,c,hset):
            h= g[r][c]
            for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:      
                rr,cc,h1= r+i,c+j,h+1          
                if 0<=rr<m and 0<=cc<n and  h1<g[rr][cc]:
                    g[rr][cc]=h1
                    hset.add((rr,cc))

        g,m,n= mat,len(mat),len(mat[0])
        m_n= m*n
        g = [ [0 if g[i][j]==0 else m_n for j in range(n)] for i in range(m)]
        hset = [(i,j) for i in range(m) for j in range(n) if g[i][j]==0]
        for h in range(0,m_n+1):
            _hset,hset=set(hset),set()
            for r,c in _hset:
                max_link(r,c,hset)
        return g        
```

[title]: https://leetcode-cn.com/problems/01-matrix
