# [One Away LCCI][title]

## Description

字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。



**示例  1:**
            **输入:**     first = "pale"    second = "ple"    **输出:** True



**示例  2:**
            **输入:**     first = "pales"    second = "pal"    **输出:** False    


**Tags:** Two Pointers, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        f,s = (first,second) if len(first)>len(second) else (second,first)
        edn=lambda a,b,n:sum(0 if a[i]==b[i] or b[i]=='.'  else 1 for i in range(len(a)) )<=n
        print(f,s)
        if len(f)==len(s):
            return edn(f,s,1)
        elif len(f)==len(s)+1:
            if len(s)==0: return edn(f,'.',0)
            for i in range(len(s)+1):
                t=s[:i]+'.'+s[i:]
                print(f,t)
                if edn(f,t,0):
                    print(f,t,0)
                    return True
            return False
        return False
```

[title]: https://leetcode-cn.com/problems/one-away-lcci
