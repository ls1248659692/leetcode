# [Spiral Matrix][title]

## Description

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)
            **输入：** matrix = [[1,2,3],[4,5,6],[7,8,9]]    **输出：** [1,2,3,6,9,8,7,4,5]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)
            **输入：** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]    **输出：** [1,2,3,4,8,12,11,10,9,5,6,7]    

**提示：**

  * `m == matrix.length`
  * `n == matrix[i].length`
  * `1 <= m, n <= 10`
  * `-100 <= matrix[i][j] <= 100`


**Tags:** Array, Matrix, Simulation

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spo(l,r,t,b):
            print(l,r,t,b)
            out =[]
            if l+1>r or t+1>b:
                return []
            elif l+1==r:
                return [g[i][l] for i in range(t,b)]
            elif t+1==b:
                return  g[t][l:r] 
            out += g[t][l:r-1]
            out += [g[i][r-1] for i in range(t,b-1)]
            out +=  g[b-1][l+1:r][::-1]
            out += [g[i][l] for i in range(b-1,t,-1)]
            return out +spo(l+1,r-1,t+1,b-1)
        g,m,n = matrix,len(matrix),len(matrix[0])
        for r in g:print(r)
        return spo(0,n,0,m)
        
```

[title]: https://leetcode-cn.com/problems/spiral-matrix
