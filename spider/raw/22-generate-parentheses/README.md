# [Generate Parentheses][title]

## Description

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。



**示例 1：**
            **输入：** n = 3    **输出：** ["((()))","(()())","(())()","()(())","()()()"]    

**示例 2：**
            **输入：** n = 1    **输出：** ["()"]    



**提示：**

  * `1 <= n <= 8`


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

[title]: https://leetcode-cn.com/problems/generate-parentheses
