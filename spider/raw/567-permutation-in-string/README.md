# [Permutation in String][title]

## Description

给你两个字符串 `s1` 和 `s2` ，写一个函数来判断 `s2` 是否包含 `s1` ** ** 的排列。如果是，返回 `true` ；否则，返回
`false` 。

换句话说，`s1` 的排列之一是 `s2` 的 **子串** 。



**示例 1：**
            **输入：** s1 = "ab" s2 = "eidbaooo"    **输出：** true    **解释：** s2 包含 s1 的排列之一 ("ba").    

**示例 2：**
            **输入：** s1= "ab" s2 = "eidboaoo"    **输出：** false    



**提示：**

  * `1 <= s1.length, s2.length <= 104`
  * `s1` 和 `s2` 仅包含小写字母


**Tags:** Hash Table, Two Pointers, String, Sliding Window

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def __init__(self):
        self.cache={}

    def permut(self,chars):
        if ''.join(sorted(chars)) in self.cache: return self.cache[''.join(sorted(chars))]
        if len(chars)==1:
            self.cache[''.join(chars)]=chars
            return chars
        else:
            rli = ['']*len(chars)
            for ii in range(len(chars)):
                rli[ii]= [chars[ii]+el for el in self.permut(chars[:ii]+chars[ii+1:])]
            pli=[]
            for rr in rli:
                pli.extend(rr)
            self.cache[''.join(sorted(chars))]=pli
            return pli

    def checkInclusion(self, s1: str, s2: str) -> bool:
        srt_s1 = sorted(list(s1))
        for ii in range(len(s2)-len(s1)+1):
            if sorted(list(s2[ii:ii+len(s1)]))==srt_s1: return True
        return False
```

[title]: https://leetcode-cn.com/problems/permutation-in-string
