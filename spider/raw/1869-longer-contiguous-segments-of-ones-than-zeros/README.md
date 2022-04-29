# [Longer Contiguous Segments of Ones than Zeros][title]

## Description

给你一个二进制字符串 `s` 。如果字符串中由 `1` 组成的 **最长** 连续子字符串 **严格长于** 由 `0` 组成的 **最长**
连续子字符串，返回 `true` ；否则，返回 `false` __ 。

  * 例如，`s = " **11** 01 **000** 10"` 中，由 `1` 组成的最长连续子字符串的长度是 `2` ，由 `0` 组成的最长连续子字符串的长度是 `3` 。

注意，如果字符串中不存在 `0` ，此时认为由 `0` 组成的最长连续子字符串的长度是 `0` 。字符串中不存在 `1` 的情况也适用此规则。

**示例 1：**
            **输入：** s = "1101"    **输出：** true    **解释：**    由 1 组成的最长连续子字符串的长度是 2：" **11** 01"    由 0 组成的最长连续子字符串的长度是 1："11 **0** 1"    由 1 组成的子字符串更长，故返回 true 。    

**示例 2：**
            **输入：** s = "111000"    **输出：** false    **解释：**    由 1 组成的最长连续子字符串的长度是 3：" **111** 000"    由 0 组成的最长连续子字符串的长度是 3："111 **000** "    由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。    

**示例 3：**
            **输入：** s = "110100010"    **输出：** false    **解释：**    由 1 组成的最长连续子字符串的长度是 2：" **11** 0100010"    由 0 组成的最长连续子字符串的长度是 3："1101 **000** 10"    由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。    

**提示：**

  * `1 <= s.length <= 100`
  * `s[i]` 不是 `'0'` 就是 `'1'`


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s= 'a'+s+'z'
        tli =[[s[ii-1],ii] for ii in range(1,len(s)) if s[ii-1]!=s[ii]]
        t2li = [tli[ii]+[tli[ii][-1]-(tli[ii-1][-1] if ii>0 else 0)] for ii in range(len(tli))]
        print(tli,t2li)
        if not t2li:return False
        return max([t[-1]if t[0]=='1' else 0 for t in t2li ])>max([t[-1] if t[0]=='0' else 0 for t in t2li ])
```

[title]: https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros
