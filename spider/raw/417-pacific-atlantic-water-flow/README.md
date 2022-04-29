# [Pacific Atlantic Water Flow][title]

## Description

有一个 `m × n` 的长方形岛屿，与 **太平洋** 和 **大西洋** 相邻。  **“太平洋”  **处于大陆的左边界和上边界，而
**“大西洋”** 处于大陆的右边界和下边界。

这个岛被分割成一个个方格网格。给定一个 `m x n` 的整数矩阵 `heights` ， `heights[r][c]` 表示坐标 `(r, c)`
上单元格 **高于海平面的高度** 。

岛上雨水较多，如果相邻小区的高度 **小于或等于** 当前小区的高度，雨水可以直接向北、南、东、西流向相邻小区。水可以从海洋附近的任何细胞流入海洋。

返回 _网格坐标`result` 的 **2D列表** ，其中 `result[i] = [ri, ci]` 表示雨水可以从单元格 `(ri, ci)`
流向 **太平洋和大西洋**_ 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)
            **输入:** heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]    **输出:** [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]    

**示例 2：**
            **输入:** heights = [[2,1],[1,2]]    **输出:** [[0,0],[0,1],[1,0],[1,1]]    



**提示：**

  * `m == heights.length`
  * `n == heights[r].length`
  * `1 <= m, n <= 200`
  * `0 <= heights[r][c] <= 105`


**Tags:** Depth-First Search, Breadth-First Search, Array, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def subisl(grid,nlim,mlim):
            def max_link(sr,sc):
                iset,iseta =set([(sr,sc)]) ,set([(sr,sc)])
                while len(iseta):
                    _iseta,iseta=set(iseta),set()
                    for r,c in _iseta:
                        for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                            if 0<=r+i<n and 0<=c+j<m and g[r+i][c+j] >=g[r][c] and (r+i,c+j) not in iset: iseta.add((r+i,c+j))  
                    for e in iseta: iset.add(e)
                return iset

            g,n,m=grid,len(grid),len(grid[0])
            #print('n=%sm=%s'%(n,m))
            inum ,tset,islands = 0,set(),[]
            
            for r in range(n):
                for c in range(m):
                    if r !=nlim and c!=mlim:continue
                    if  (r,c) not in tset:
                        inum +=1
                        iset = max_link(r,c)
                        for e in iset: tset.add(e)
                        #print('iset=%s'%iset)
                        islands.append(sorted(list(iset)))
            return islands 

        g,n,m=heights,len(heights),len(heights[0])
        pset,aset=set(),set()       
        tset = subisl(g,0,0)
        for pa in tset: 
            # print(pa)
            for e in pa:pset.add(e)

        tset = subisl(g,n-1,m-1)
        for pa in tset: 
            for e in pa:aset.add(e) 
                
        print([(g[x][y],x,y) for x,y in pset ])
        print([(g[x][y],x,y) for x,y in aset ])
        return  [[x,y] for x,y in pset & aset ]          

```

[title]: https://leetcode-cn.com/problems/pacific-atlantic-water-flow
