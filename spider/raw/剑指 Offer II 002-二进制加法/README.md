# [二进制加法][title]

## Description

给定两个 01 字符串 `a` 和 `b` ，请计算它们的和，并以二进制字符串的形式输出。

输入为 **非空** 字符串且只包含数字 `1` 和 `0`。



**示例  1:**
            **输入:** a = "11", b = "10"    **输出:** "101"

**示例  2:**
            **输入:** a = "1010", b = "1011"    **输出:** "10101"



**提示：**

  * 每个字符串仅由字符 `'0'` 或 `'1'` 组成。
  * `1 <= a.length, b.length <= 10^4`
  * 字符串如果不是 `"0"` ，就都不含前导零。



注意：本题与主站 67 题相同：<https://leetcode-cn.com/problems/add-binary/>


**Tags:** Bit Manipulation, Math, String, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ma = a if len(a) > len(b) else b
        mi = b if len(a) > len(b) else a
        mi = '0' * (len(ma) - len(mi)) + mi
        tli = ['0' for i in range(len(ma) + 1)]
        for i in range(1, len(mi) + 1):
            su = sum([int(mi[-i]), int(ma[-i]), int(tli[-i])])
            tli[-i] = str(su % 2)
            tli[-i - 1] = str(su // 2)
        r = (''.join(tli))
        if not r: return ''
        while len(r) > 1 and r[0] == '0': r = r[1:]
        return r        
```

[title]: https://leetcode-cn.com/problems/JFETK5
