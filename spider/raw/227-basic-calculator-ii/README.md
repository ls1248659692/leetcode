# [Basic Calculator II][title]

## Description

给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。

**示例 1：**
            **输入：** s = "3+2*2"    **输出：** 7    

**示例 2：**
            **输入：** s = " 3/2 "    **输出：** 1    

**示例 3：**
            **输入：** s = " 3+5 / 2 "    **输出：** 5    

**提示：**

  * `1 <= s.length <= 3 * 105`
  * `s` 由整数和算符 `('+', '-', '*', '/')` 组成，中间由一些空格隔开
  * `s` 表示一个 **有效表达式**
  * 表达式中的所有整数都是非负整数，且在范围 `[0, 231 - 1]` 内
  * 题目数据保证答案是一个 **32-bit 整数**


**Tags:** Stack, Math, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def calculate(self, s: str) -> int:
        sli=[el for el in s.replace(' ','').replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').split() if el]
        #sli0 = list(sli)
        while '*' in sli or '/' in sli:
            for n in range(len(sli)):
                if sli[n] in ('*','/'):
                    sli[n-1] = str(int(sli[n-1]) *int(sli[n+1]) if sli[n]=='*' else int(sli[n-1]) //int(sli[n+1]))
                    sli[n],sli[n+1] ='','' 
                    break               
            sli = [el for el in sli if el]
            
        sstr= ''.join(sli).replace('-','+-')
        ssli = sstr.split('+')
        return sum(int(el) for el in ssli)

        while '+' in sli or '-' in sli:
            for n in range(len(sli)):
                if sli[n] in ('+','-'):
                    sli[n-1] = str(int(sli[n-1]) +int(sli[n+1]) if sli[n]=='+' else int(sli[n-1]) -int(sli[n+1]))
                    sli[n],sli[n+1] ='',''
                    break
            sli = [el for el in sli if el]
        print(''.join(sli))
        return int(''.join(sli))
        #return eval(s.replace('/','//'))
```

[title]: https://leetcode-cn.com/problems/basic-calculator-ii
