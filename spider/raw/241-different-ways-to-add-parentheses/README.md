# [Different Ways to Add Parentheses][title]

## Description

给你一个由数字和运算符组成的字符串 `expression` ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 **按任意顺序**
返回答案。



**示例 1：**
            **输入：** expression = "2-1-1"    **输出：** [0,2]    **解释：**    ((2-1)-1) = 0     (2-(1-1)) = 2    

**示例 2：**
            **输入：** expression = "2*3-4*5"    **输出：** [-34,-14,-10,-10,10]    **解释：**    (2*(3-(4*5))) = -34     ((2*3)-(4*5)) = -14     ((2*(3-4))*5) = -10     (2*((3-4)*5)) = -10     (((2*3)-4)*5) = 10    



**提示：**

  * `1 <= expression.length <= 20`
  * `expression` 由数字和算符 `'+'`、`'-'` 和 `'*'` 组成。
  * 输入表达式中的所有整数值在范围 `[0, 99]` 


**Tags:** Recursion, Memoization, Math, String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def sp(s):
            rli =['']
            for c in s:
                if c in ['-','+','*']:
                    rli.append(c)
                    rli.append('')
                else:
                    rli[-1]+=c
            #rli.append('.')
            return rli

        def calc(ls1,ls2,c):
            if c=='+': return [n+m for n in ls1 for m in ls2]
            if c=='-': return [n-m for n in ls1 for m in ls2]
            if c=='*': return [n*m for n in ls1 for m in ls2]

        sl = sp(expression)
        print(sl)

        def dfw(sl):
            r = []
            if not sl:return [0]
            elif len(sl)==1: return [int(sl[0])]
            else:
                for i in range(1,len(sl),2):
                    r+=calc(dfw(sl[:i]),dfw(sl[i+1:]),sl[i])
            return r
        return dfw(sl)

            
```

[title]: https://leetcode-cn.com/problems/different-ways-to-add-parentheses
