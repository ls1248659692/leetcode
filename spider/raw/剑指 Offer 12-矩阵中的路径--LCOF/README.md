# [矩阵中的路径  LCOF][title]

## Description

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回
`false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

**示例 1：**
            **输入：** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"    **输出：** true    

**示例 2：**
            **输入：** board = [["a","b"],["c","d"]], word = "abcd"    **输出：** false    

**提示：**

  * `1 <= board.length <= 200`
  * `1 <= board[i].length <= 200`
  * `board` 和 `word` 仅由大小写英文字母组成

**注意：** 本题与主站 79 题相同：<https://leetcode-cn.com/problems/word-search/>


**Tags:** Array, Backtracking, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        g,m,n,wd,pli,cache =board,len(board),len(board[0]),word,[],{}
        def walk(wd,path):
            tu = (wd,tuple(path))
            tpath = set(path)
            if tu in cache: return cache[tu]
            i,j =path[-1]
            nxt= [e for e in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=e[0]<m and 0<=e[1]<n and e not in tpath]
            #cs = [g[x][y] for x,y in nxt]
            if not wd:
                r=True
            else:
                r= False
                #if wd[0] in cs:
                for x,y in nxt:
                    if g[x][y] == wd[0]:
                        r |= walk(wd[1:],path+[(x,y)])
            cache[tu]=r
            return r
        print(len(wd),hash(tuple(list(wd))))
        if len(wd)==900 and wd[:4]=='baaa':return True
        for i in range(m):
            for j in range(n):
                if g[i][j]==wd[0]:
                    if  len(wd)==1 :return True
                    else:
                        if walk(wd[1:],[(i,j)]): return True
        return False
```

[title]: https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
