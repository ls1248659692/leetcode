# [Find the Closest Palindrome][title]

## Description

给定一个表示整数的字符串 `n` ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

“最近的”定义为两个整数 **差的绝对值** 最小。



**示例 1:**
            **输入:** n = "123"    **输出:** "121"    

**示例 2:**
            **输入:** n = "1"    **输出:** "0"    **解释:** 0 和 2是最近的回文，但我们返回最小的，也就是 0。    



**提示:**

  * `1 <= n.length <= 18`
  * `n` 只由数字组成
  * `n` 不含前导 0
  * `n` 代表在 `[1, 1018 - 1]` 范围内的整数


**Tags:** Math, String

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        ll, intn = len(n), int(n)
        if ll == 1: return str(intn - 1)
        candlist = [int('9'*(ll-1) if (ll-1) else '0'), int('1'+'0'*(ll-1)+'1'), int(n[:ll // 2] + n[(ll - 1) // 2::-1])]
        halfn = int(n[:(ll + 1) // 2])
        candlist += [int(str(halfn - 1) + str(halfn - 1)[- 1 - ll % 2::-1])] if halfn != 10 ** ((ll - 1) // 2) else []
        candlist += [int(str(halfn + 1) + str(halfn + 1)[- 1 - ll % 2::-1])] if str(halfn) != '9' * ((ll + 1) // 2 + 1) else []
        candlist.sort()
        return str([cc for cc in candlist if abs(cc - intn) == min([abs(cc - intn) for cc in candlist if abs(cc - intn) != 0])][0])
```

[title]: https://leetcode-cn.com/problems/find-the-closest-palindrome
