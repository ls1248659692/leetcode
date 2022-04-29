# [Minimum Add to Make Parentheses Valid][title]

## Description

给定一个由 `'('` 和 `')'` 括号组成的字符串 `S`，我们需要添加最少的括号（ `'('` 或是
`')'`，可以在任何位置），以使得到的括号字符串有效。

从形式上讲，只有满足下面几点之一，括号字符串才是有效的：

  * 它是一个空字符串，或者
  * 它可以被写成 `AB` （`A` 与 `B` 连接）, 其中 `A` 和 `B` 都是有效字符串，或者
  * 它可以被写作 `(A)`，其中 `A` 是有效字符串。

给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。



**示例 1：**
            **输入：** "())"    **输出：** 1    

**示例 2：**
            **输入：** "((("    **输出：** 3    

**示例 3：**
            **输入：** "()"    **输出：** 0    

**示例 4：**
            **输入：** "()))(("    **输出：** 4



**提示：**

  1. `S.length <= 1000`
  2. `S` 只包含 `'('` 和 `')'` 字符。




**Tags:** Stack, Greedy, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #this one
        def rp(s):
            n = 0
            pn = []
            for i in range(len(s)):
                c= s[i]
                if c=='(':n+=1
                pn.append(-n if s[i:i+2]==')(' or s[i-1:i+1]==')(' else n )
                if c==')':n-=1
            return pn
                    
        while '()' in s: s=s.replace('()','')
        print(s)
        return len(s)
```

[title]: https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid
