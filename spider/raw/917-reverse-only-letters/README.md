# [Reverse Only Letters][title]

## Description

给你一个字符串 `s` ，根据下述规则反转字符串：

  * 所有非英文字母保留在原有位置。
  * 所有英文字母（小写或大写）位置反转。

返回反转后的 `s` _。_



**示例 1：**
            **输入：** s = "ab-cd"    **输出：** "dc-ba"    

**示例 2：**
            **输入：** s = "a-bC-dEf-ghIj"    **输出：** "j-Ih-gfE-dCba"    

**示例 3：**
            **输入：** s = "Test1ng-Leet=code-Q!"    **输出：** "Qedo1ct-eeLg=ntse-T!"    



**提示**

  * `1 <= s.length <= 100`
  * `s` 仅由 ASCII 值在范围 `[33, 122]` 的字符组成
  * `s` 不含 `'\"'` 或 `'\\'`


**Tags:** Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sli = list(s)
        tli =[i for i in range(len(s)) if s[i].isalpha()]
        for i in range(1,len(tli)//2+1):
            sli[tli[i-1]], sli[tli[-i]]= sli[tli[-i]],sli[tli[i-1]]
        return ''.join(sli)

```

[title]: https://leetcode-cn.com/problems/reverse-only-letters
