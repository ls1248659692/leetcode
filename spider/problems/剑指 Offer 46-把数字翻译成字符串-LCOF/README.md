# [把数字翻译成字符串 LCOF][title]

## Description

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 "a" ，1 翻译成 "b"，……，11 翻译成 "l"，……，25 翻译成
"z"。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。



**示例 1:**
            **输入:** 12258    **输出:** 5    **解释:** 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"



**提示：**

  * `0 <= num < 231`


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def __init__(self):
        self.d1 = [str(el) for el in range(10)]
        self.d2 = [str(el) for el in range(10,26)]
        self.cache ={}
        self.cache.update({kk:1 for kk in self.d1})

    def t_num(self,pstr):
        #print('t_num',pstr)
        if pstr in self.cache:return self.cache[pstr]
        if len(pstr)==1:
            r= 1
        elif len(pstr)==2:
            r= 2 if pstr in self.d2 else 1
        else:
            r1 = self.t_num(pstr[1:])
            r2 = self.t_num(pstr[2:]) if pstr[:2] in self.d2 else 0
            r = r1+r2
        self.cache[pstr]=r
        return r

    def translateNum(self, num: int) -> int:
        return self.t_num(str(num))
```

[title]: https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
