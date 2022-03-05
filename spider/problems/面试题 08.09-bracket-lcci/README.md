# [Bracket LCCI][title]

## Description

括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：
            [      "((()))",      "(()())",      "(())()",      "()(())",      "()()()"    ]    


**Tags:** String, Dynamic Programming, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dic={'(':0,')':0}
        tli =['(']
        for ii in range(1,n*2):
            tmpli=[]
            tmpli += [el+'(' for el in tli if el.count('(')<n]
            tmpli += [el+')' for el in tli if el.count('(')-el.count(')')>0]
            tli = tmpli
            print(tli)
        return tli        
```

[title]: https://leetcode-cn.com/problems/bracket-lcci
