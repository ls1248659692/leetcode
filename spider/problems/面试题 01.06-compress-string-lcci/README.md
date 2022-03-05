# [Compress String LCCI][title]

## Description

字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串`aabcccccaaa`会变为`a2b1c5a3`。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

**示例1:**
            **输入** ："aabcccccaaa"    **输出** ："a2b1c5a3"    

**示例2:**
            **输入** ："abbccd"    **输出** ："abbccd"    **解释** ："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。    

**提示：**

  1. 字符串长度在[0, 50000]范围内。


**Tags:** Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def compressString(self, S: str) -> str:
        def dsplit(s):
            rli = [[1,s[0]]]
            for c in s[1:]:
                if c== rli[-1][-1]:rli[-1][0]+=1
                else: rli.append([1,c])
            return rli

        if not S: return ''     
        sli = dsplit(S)
        return ''.join([e[1]+str(e[0]) for e in sli ]) if len(sli)*2<len(S) else S
```

[title]: https://leetcode-cn.com/problems/compress-string-lcci
