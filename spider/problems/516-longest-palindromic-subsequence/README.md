# [Longest Palindromic Subsequence][title]

## Description

给你一个字符串 `s` ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

**示例 1：**
            **输入：** s = "bbbab"    **输出：** 4    **解释：** 一个可能的最长回文子序列为 "bbbb" 。    

**示例 2：**
            **输入：** s = "cbbd"    **输出：** 2    **解释：** 一个可能的最长回文子序列为 "bb" 。    

**提示：**

  * `1 <= s.length <= 1000`
  * `s` 仅由小写英文字母组成


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def clr(left,right):
            d={}
            for i in range(left,right):
                c=s[i]
                d.setdefault(c,[])
                d[c].append(i)
            return d.items()

        def out(it,left,right):
            t = []
            n_it=[]
            for c,li in it:
                tli = [e for e in li if left<=e<right]
                n_it.append((c,tli))
                if len(tli)>=2: t.append((c,tli[0],tli[-1]))

            if not t: return [],[]
            t = sorted(t,key=lambda xx:xx[1])
            min_r = t[0][-1]
            ou=[t[0]]
            for i in range(1,len(t)):
                if t[i][-1]<min_r: 
                    min_r= t[i][-1]
                else:
                    ou.append(t[i])
            return ou,n_it

        def lop(it,left,right):# [left,right)
            if right-left==0:return 0
            if (left,right) in cache:return cache[(left,right)]
            ou,it = out(it,left,right)
            res= max([lop(it,i+1,j) if j>i else 0 for c,i,j in ou ])+2 if ou else 1
            cache[(left,right)]=res
            return res
        cache={}
        ou,it =out(clr(0,len(s)),0,len(s))
        mx= lop(it,0,len(s))
        return mx
```

[title]: https://leetcode-cn.com/problems/longest-palindromic-subsequence
