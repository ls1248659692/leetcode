# [Boolean Evaluation LCCI][title]

## Description

给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 `0` (false)、`1` (true)、`&` (AND)、 `|` (OR) 和
`^` (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。

**示例 1:**
            **输入:** s = "1^0|0|1", result = 0        **输出:** 2    **解释:**  两种可能的括号方法是    1^(0|(0|1))    1^((0|0)|1)    

**示例 2:**
            **输入:** s = "0&0&0&1^1|0", result = 1        **输出:** 10

**提示：**

  * 运算符的数量不超过 19 个


**Tags:** Memoization, String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def countEval(self, s: str, result: int) -> int:
        expression =s
        def sp(s):
            rli =['']
            for c in s:
                if c in ['|','&','^']:
                    rli.append(c)
                    rli.append('')
                else:
                    rli[-1]+=c
            return rli

        # def calc(ls1,ls2,c,r):
        #     len1,len2= len(ls1),
        #     if r==1:
        #         if c=='|': return [n|m for n in ls1 for m in ls2]
        #         if c=='&': return [n&m for n in ls1 for m in ls2]
        #         if c=='^': return [n^m for n in ls1 for m in ls2]
        T,F=True,False
        def calc(d1,d2,c):
            d1['A']=d1[T]+d1[F]
            d2['A']=d2[T]+d2[F]
            tot =d1['A']*d2['A']
            if c=='|': return {True:d1[T]*d2['A']+d2[T]*d1['A']-d1[T]*d2[T], False:tot-d1[T]*d2['A']-d2[T]*d1['A']+d1[T]*d2[T]}
            if c=='&': return {True:d1[T]*d2[T], False:tot-d1[T]*d2[T]}
            if c=='^': return {True:d1[T]*d2[F]+d1[F]*d2[T], False:tot-d1[T]*d2[F]-d1[F]*d2[T]}

        sl = sp(expression)
        print(sl)
        cache={}

        def dfw(sl):
            tsl= tuple(sl)
            if tsl in cache:return cache[tsl]
            r = {T:0,F:0}
            if len(sl)==1: r= {T:1,F:0} if int(sl[0]) else {T:0,F:1} 
            else:
                for i in range(1,len(sl),2):
                    m=calc(dfw(sl[:i]),dfw(sl[i+1:]),sl[i])
                    r[T],r[F]=r[T]+m[T],r[F]+m[F]
            cache[tsl]=r
            return r
        d=  dfw(sl)
        return d[T if result else F]

```

[title]: https://leetcode-cn.com/problems/boolean-evaluation-lcci
