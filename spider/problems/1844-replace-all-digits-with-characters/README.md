# [Replace All Digits with Characters][title]

## Description

给你一个下标从 **0** 开始的字符串 `s` ，它的 **偶数** 下标处为小写英文字母， **奇数** 下标处为数字。

定义一个函数 `shift(c, x)` ，其中 `c` 是一个字符且 `x` 是一个数字，函数返回字母表中 `c` 后面第 `x` 个字符。

  * 比方说，`shift('a', 5) = 'f'` 和 `shift('x', 0) = 'x'` 。

对于每个 **奇数** 下标 `i` ，你需要将数字 `s[i]` 用 `shift(s[i-1], s[i])` 替换。

请你替换所有数字以后，将字符串 `s` 返回。题目 **保证** __`shift(s[i-1], s[i])` 不会超过 `'z'` 。

**示例 1：**
            **输入：** s = "a1c1e1"    **输出：** "abcdef"    **解释：** 数字被替换结果如下：    - s[1] -> shift('a',1) = 'b'    - s[3] -> shift('c',1) = 'd'    - s[5] -> shift('e',1) = 'f'

**示例 2：**
            **输入：** s = "a1b2c3d4e"    **输出：** "abbdcfdhe"    **解释：** 数字被替换结果如下：    - s[1] -> shift('a',1) = 'b'    - s[3] -> shift('b',2) = 'd'    - s[5] -> shift('c',3) = 'f'    - s[7] -> shift('d',4) = 'h'

**提示：**

  * `1 <= s.length <= 100`
  * `s` 只包含小写英文字母和数字。
  * 对所有 **奇数** 下标处的 `i` ，满足 `shift(s[i-1], s[i]) <= 'z'` 。


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def replaceDigits(self, s: str) -> str:
        return ''.join([ chr(ord(s[ii-1])+int(s[ii])) if ii%2==1 else s[ii] for ii in range(len(s))])
```

[title]: https://leetcode-cn.com/problems/replace-all-digits-with-characters
