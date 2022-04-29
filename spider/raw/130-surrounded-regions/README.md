# [Surrounded Regions][title]

## Description

给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` ，找到所有被 `'X'` 围绕的区域，并将这些区域里所有的
`'O'` 用 `'X'` 填充。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)
            **输入：** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]    **输出：** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]    **解释：** 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。    

**示例 2：**
            **输入：** board = [["X"]]    **输出：** [["X"]]    

**提示：**

  * `m == board.length`
  * `n == board[i].length`
  * `1 <= m, n <= 200`
  * `board[i][j]` 为 `'X'` 或 `'O'`


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Array, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def max_link(g,sr,sc):
            aset,tset =set([(sr,sc)]) ,set([(sr,sc)])
            while aset:
                _aset,aset=set(aset),set()
                for r,c in _aset:
                    for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if 0<=r+i<m and 0<=c+j<n and g[r+i][c+j] ==g[sr][sc] and (r+i,c+j) not in tset:
                             aset.add((r+i,c+j))     
                    for p in aset:tset.add(p)
            return tset

        g,m,n=board,len(board),len(board[0])
        for r in g:print(r)
        inum ,tset,islands = 0,set(),[]
        
        for r in range(m):
            for c in range(n):
                if g[r][c]=='O' and (r,c) not in tset:
                    inum +=1
                    iset = max_link(g,r,c)
                    tset =tset.union(iset )
                    islands.append(iset)
        for isl in islands:
            if sum([1 for x,y in isl if x in (0,m-1) or y in (0,n-1)])==0:
                for x,y in isl:
                    board[x][y]='X'
        print('

')            
        for r in board:print(r)
        # cnt=sum(sum([1 for x,y in isl if x in (0,n-1) or y in (0,m-1)])==0 for isl in islands)
        # return sum(len(isl) for isl in islands if sum([1 for x,y in isl if x in (0,n-1) or y in (0,m-1)])==0) if islands else 0        
```

[title]: https://leetcode-cn.com/problems/surrounded-regions
