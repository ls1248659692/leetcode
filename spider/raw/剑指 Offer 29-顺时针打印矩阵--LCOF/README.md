# [顺时针打印矩阵  LCOF][title]

## Description

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



**示例 1：**
            **输入：** matrix = [[1,2,3],[4,5,6],[7,8,9]]    **输出：** [1,2,3,6,9,8,7,4,5]    

**示例 2：**
            **输入：** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]    **输出：** [1,2,3,4,8,12,11,10,9,5,6,7]    



**限制：**

  * `0 <= matrix.length <= 100`
  * `0 <= matrix[i].length <= 100`

注意：本题与主站 54 题相同：<https://leetcode-cn.com/problems/spiral-matrix/>


**Tags:** Array, Matrix, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def rc(x,ij):
            return [[ij[0], j ] for j in range(x)] if ij[1] is None else [[j,ij[1] ] for j in range(x)]
        ma =matrix
        if not ma:return[]
        m,n = len(ma[0]),len(ma)
        for r in ma:print(r)
        rli =[]

        while m>1 and n>1:
            tli = rc(m,[0,None])+ rc(n,[None,m-1])[1:-1] + rc(m,[n-1,None])[::-1] + rc(n,[None,0])[1:-1][::-1]
            #tli= [[0, j ] for j in range(m)] +[[i,m-1] for i in range(n)][1:-1] +[[n-1,j] for j in range(m)][::-1]+[[i,0] for i in range(n)][1:-1][::-1]
            rli += [ma[p[0]][p[1]] for p in tli]
            ma = [r[1:-1] for r in ma[1:-1] ]
            m,n = len(ma[0]) if ma else 0,len(ma)   
        rli+=[el for r in ma for el in r]
        return rli
```

[title]: https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
