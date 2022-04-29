# [N-Queens][title]

## Description

**n  皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的  **n _ _ 皇后问题** 的解决方案。

每一种解法包含一个不同的  **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
            **输入：** n = 4    **输出：** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]    **解释：** 如上图所示，4 皇后问题存在两个不同的解法。    

**示例 2：**
            **输入：** n = 1    **输出：** [["Q"]]    



**提示：**

  * `1 <= n <= 9`


**Tags:** Array, Backtracking

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res =[]
        def ck_rule(i,j,ocups):
            for oci,ocj in ocups:
                if oci==i or ocj==j or oci+ocj==i+j or i-oci==j-ocj:return False
            return True

        for i in range(n):
            res0 = res.copy()
            #print('res0=%s len(res0)=%s '%(res0,len(res0)))
            for j in range(n):
                if not res0:
                    res.append([(i,j)])
                else:
                    #print('res0=%s len(res0)=%s'%(res0,len(res0)))
                    for o in range(len(res0)):
                        ocups=res0[o]
                        if ocups and ck_rule(i,j,ocups):
                            res.append(res[o]+[(i,j)])
                            #print(res[o],len(res[o]))
   
            res = [el for el in res if len(el)==i+1]

        def qb(i):
            return ''.join(['Q' if m==i else '.' for m in range(n)])
        res = [ [qb(r[1]) for r in re] for re in res  ]
        print(res)
        return res
```

[title]: https://leetcode-cn.com/problems/n-queens
