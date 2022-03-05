# [字符串的排列  LCOF][title]

## Description

输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



**示例:**
            **输入：** s = "abc"    **输出：[** "abc","acb","bac","bca","cab","cba" **]**    



**限制：**

`1 <= s 的长度 <= 8`


**Tags:** String, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def perm_k(self,pstr):
        res = ['']
        if  pstr:
            for ii in range(len(pstr)):
                res += [pstr[ii]+ el for el in self.perm_k(pstr[:ii]+pstr[ii+1:])]
        return res

    def permutation(self, s: str) -> List[str]:
        res =self.perm_k(s)
        return list(set([el for el in res if len(el)==len(s)]))
```

[title]: https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
