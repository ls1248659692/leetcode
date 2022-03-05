# [Word Search][title]

## Description

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回
`false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)
            **输入：** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)
            **输入：** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"    **输出：** true    

**示例 3：**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)
            **输入：** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"    **输出：** false    

**提示：**

  * `m == board.length`
  * `n = board[i].length`
  * `1 <= m, n <= 6`
  * `1 <= word.length <= 15`
  * `board` 和 `word` 仅由大小写英文字母组成

**进阶：** 你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？


**Tags:** Array, Backtracking, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        g,n,m,wd,pli =board,len(board),len(board[0]),word,[]
        def walk(wd,path):
            i,j =path[-1]
            nxt= [e for e in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=e[0]<n and 0<=e[1]<m and e not in path]
            cs = [g[e[0]][e[1]] for e in nxt]
            #print(cs,wd)
            if wd[0] in cs:
                for pt in nxt:
                    if g[pt[0]][pt[1]] == wd[0]:
                        path1 = path+[pt]
                        #print(wd,path1)
                        if len(wd)>1:walk(wd[1:],path1)
                        #if len(path1)==7: print(wd,path1)
                        pli.append(len(path1))
                return None

            #return path
        #walk(wd[1:],[(0,0)])
        #return
        for i in range(n):
            for j in range(m):
                if g[i][j]==wd[0]:
                    if  len(wd)==1 :return True
                    else:
                        walk(wd[1:],[(i,j)])
                #print(pli)
        return max([p for p in pli])==len(wd) if pli else False
```

[title]: https://leetcode-cn.com/problems/word-search
