# [Backspace String Compare][title]

## Description

给定 `s` 和 `t` 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 `true` 。`#` 代表退格字符。

**注意：** 如果对空文本输入退格字符，文本继续为空。



**示例 1：**
            **输入：** s = "ab#c", t = "ad#c"    **输出：** true    **解释：** s 和 t 都会变成 "ac"。    

**示例 2：**
            **输入：** s = "ab##", t = "c#d#"    **输出：** true    **解释：** s 和 t 都会变成 ""。    

**示例 3：**
            **输入：** s = "a#c", t = "b"    **输出：** false    **解释：** s 会变成 "c"，但 t 仍然是 "b"。



**提示：**

  * `1 <= s.length, t.length <= 200`
  * `s` 和 `t` 只含有小写字母以及字符 `'#'`



**进阶：**

  * 你可以用 `O(n)` 的时间复杂度和 `O(1)` 的空间复杂度解决该问题吗？


**Tags:** Stack, Two Pointers, String, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def bs(s):
            nli=[]
            for c in s:
                if c=='#':
                    if nli:nli.pop()
                else: 
                    nli.append(c)
            print (''.join(nli))
            return ''.join(nli)
        return bs(s)==bs(t)
```

[title]: https://leetcode-cn.com/problems/backspace-string-compare
