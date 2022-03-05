# [Knight Probability in Chessboard][title]

## Description

在一个 `n x n` 的国际象棋棋盘上，一个骑士从单元格 `(row, column)` 开始，并尝试进行 `k` 次移动。行和列是 **从 0 开始**
的，所以左上单元格是 `(0,0)` ，右下单元格是 `(n - 1, n - 1)` 。

象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/10/12/knight.png)

每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 `k` 步或离开了棋盘。

返回 _骑士在棋盘停止移动后仍留在棋盘上的概率_ 。



**示例 1：**
            **输入:** n = 3, k = 2, row = 0, column = 0    **输出:** 0.0625    **解释:** 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。    在每一个位置上，也有两种移动可以让骑士留在棋盘上。    骑士留在棋盘上的总概率是0.0625。    

**示例 2：**
            **输入:** n = 1, k = 0, row = 0, column = 0    **输出:** 1.00000    



**提示:**

  * `1 <= n <= 25`
  * `0 <= k <= 100`
  * `0 <= row, column <= n`


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def v0(n,k,row,column):
            tli=[0]
            cache={}
            def ktp(k,r,c):
                if k==0: tli[-1]+=0
                else:
                    if (k,r,c) in cache: 
                        return cache[(k,r,c)]
                    else:
                        inls =[]
                        for x,y in [(2,1),(1,2),(-2,1),(1,-2),(-2,-1),(-1,-2),(2,-1),(-1,2)]:
                            if (0<=r+x<n and 0<=c+y<n):
                                inls.append((r+x,c+y))
                        tli[-1]+= (8-len(inls))*8**(k-1)
                        for r,c in inls:
                            inls+=ktp(k-1,r,c)
                    cache[(k,r,c)] = inls 
                    return inls
            ktp(k,row,column)
            return (8**k-tli[0])/8**k

        def v1(n,k,row,column):
            cache={}
            def ktp(k,r,c):
                inn,out=0,0
                if k==0: return 1,0
                else:
                    if (k,r,c) in cache: 
                        return cache[(k,r,c)] 
                    else:
                        inls =[]
                        for x,y in [(2,1),(1,2),(-2,1),(1,-2),(-2,-1),(-1,-2),(2,-1),(-1,2)]:
                            if (0<=r+x<n and 0<=c+y<n):
                                inls.append((r+x,c+y))
                        out+= (8-len(inls))*8**(k-1)
                        for r1,c1 in inls:
                            _inn,_out=ktp(k-1,r1,c1)  if (k-1,r1,c1) not in cache else cache[(k-1,r1,c1)]
                            inn,out=inn+_inn, out+_out
                        cache[(k,r,c)] =inn,out
                    return cache[(k,r,c)] 
            inn,out=ktp(k,row,column)
            #print(inn,out)
            return inn/(inn+out)
        
        def v2(n,k,row,column):
            @cache
            def ktp(k,row,col):
                if k == 0:
                    return 1
                inls = 0
                for x, y in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                    r, c= row + x, col + y
                    if (0 <= r < n and 0 <= c < n):
                        inls += ktp(k - 1, r, c)
                return inls
            return ktp(k, row, column) / (8**k)
        return v1(n,k,row,column)
```

[title]: https://leetcode-cn.com/problems/knight-probability-in-chessboard
