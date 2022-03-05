# [Letter Case Permutation][title]

## Description

给定一个字符串 `s` ，通过将字符串 `s` 中的每个字母转变大小写，我们可以获得一个新的字符串。

返回 _所有可能得到的字符串集合_ 。以 **任意顺序** 返回输出。



**示例 1：**
            **输入：** s = "a1b2"    **输出：** ["a1b2", "a1B2", "A1b2", "A1B2"]    

**示例 2:**
            **输入:** s = "3z4"    **输出:** ["3z4","3Z4"]    



**提示:**

  * `1 <= s.length <= 12`
  * `s` 由小写英文字母、大写英文字母和数字组成


**Tags:** Bit Manipulation, String, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        r=[s[0].lower(),s[0].upper()] if s[0].isalpha() else [s[0]]
        for i in range(1,len(s)):
            r= [e+s[i].upper() for e in r] +([e+s[i].lower() for e in r]  if s[i].isalpha()else [])
        return r
```

[title]: https://leetcode-cn.com/problems/letter-case-permutation
