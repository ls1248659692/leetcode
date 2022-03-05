# [Reverse Vowels of a String][title]

## Description

给你一个字符串 `s` ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 `'a'`、`'e'`、`'i'`、`'o'`、`'u'`，且可能以大小写两种形式出现。



**示例 1：**
            **输入：** s = "hello"    **输出：** "holle"    

**示例 2：**
            **输入：** s = "leetcode"    **输出：** "leotcede"



**提示：**

  * `1 <= s.length <= 3 * 105`
  * `s` 由 **可打印的 ASCII** 字符组成


**Tags:** Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def reverseVowels(self, s: str) -> str:
        sli = list(s)
        vli = [[i,s[i]] for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        vr = [el[-1] for el in vli]
        vr = vr[::-1]
        for v in range(len(vli)):
            sli[vli[v][0]]=vr[v]
        return ''.join(sli)
```

[title]: https://leetcode-cn.com/problems/reverse-vowels-of-a-string
