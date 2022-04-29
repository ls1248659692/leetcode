# [Valid Parentheses][title]

## Description

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

  1. 左括号必须用相同类型的右括号闭合。
  2. 左括号必须以正确的顺序闭合。

**示例 1：**
            **输入：** s = "()"    **输出：** true    

**示例 2：**
            **输入：** s = "()[]{}"    **输出：** true    

**示例 3：**
            **输入：** s = "(]"    **输出：** false    

**示例 4：**
            **输入：** s = "([)]"    **输出：** false    

**示例 5：**
            **输入：** s = "{[]}"    **输出：** true

**提示：**

  * `1 <= s.length <= 104`
  * `s` 仅由括号 `'()[]{}'` 组成


**Tags:** Stack, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s=s.replace('()','').replace('[]','').replace('{}','')
        return True if s=='' else False
        
        t = ''
        for c in s:
            if c in '({[':t+=c
            else:
                if not t: return False
                elif  t[-1]!={']':'[',')':'(','}':'{'}[c]:return False
                else: t = t[:-1]
        return True if t=='' else False
```

[title]: https://leetcode-cn.com/problems/valid-parentheses
