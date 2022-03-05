# [Eight Queens LCCI][title]

## Description

设计一种算法，打印 N 皇后在 N × N
棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的"对角线"指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

**注意：** 本题相对原题做了扩展

**示例:**
            **输入** ：4    **输出** ：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]    **解释** : 4 皇后问题存在如下两个不同的解法。    [     [".Q..",  // 解法 1      "...Q",      "Q...",      "..Q."],         ["..Q.",  // 解法 2      "Q...",      "...Q",      ".Q.."]    ]    


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
            res = [el for el in res if len(el)==i+1]

        def qb(i):
            return ''.join(['Q' if m==i else '.' for m in range(n)])
        res = [ [qb(r[1]) for r in re] for re in res  ]
        print(res)
        return res        
```

[title]: https://leetcode-cn.com/problems/eight-queens-lcci
