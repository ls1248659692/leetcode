# [Decode Ways][title]

## Description

一条包含字母 `A-Z` 的消息通过以下映射进行了 **编码** ：
            'A' -> "1"    'B' -> "2"    ...    'Z' -> "26"

要 **解码** 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，`"11106"` 可以映射为：

  * `"AAJF"` ，将消息分组为 `(1 1 10 6)`
  * `"KJF"` ，将消息分组为 `(11 10 6)`

注意，消息不能分组为  `(1 11 06)` ，因为 `"06"` 不能映射为 `"F"` ，这是由于 `"6"` 和 `"06"` 在映射中并不等价。

给你一个只含数字的 **非空** 字符串 `s` ，请计算并返回 **解码** 方法的 **总数** 。

题目数据保证答案肯定是一个 **32 位** 的整数。



**示例 1：**
            **输入：** s = "12"    **输出：** 2    **解释：** 它可以解码为 "AB"（1 2）或者 "L"（12）。    

**示例 2：**
            **输入：** s = "226"    **输出：** 3    **解释：** 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。    

**示例 3：**
            **输入：** s = "0"    **输出：** 0    **解释：** 没有字符映射到以 0 开头的数字。    含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。    由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。    



**提示：**

  * `1 <= s.length <= 100`
  * `s` 只包含数字，并且可能包含前导零。


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def __init__(self):
        self.d1 = [str(el) for el in range(1,10)]
        self.d2 = [str(el) for el in range(10,27)]
        self.cache={}
        self.cache.update({dd:1 for dd in self.d1})

    def numDecodings(self, s: str) -> int:
        r = 1
        len_s = len(s)
        if s in self.cache:return self.cache[s]
        if len_s==1:
            return 1 if  s in self.d1 else 0
        elif len_s==2:
            t2 = 1 if s[:2] in self.d2 else 0
            t1 = 1 if s[0] in self.d1 and s[1] in self.d1 else 0
            return t2+t1
        else:
            r1 = (r*self.numDecodings(s[1:])) if s[0] in self.d1 else 0
            r2 = (r*self.numDecodings(s[2:])) if s[:2] in self.d2 else 0
            r= r1+r2
        self.cache[s]=r
        #print(s,r)
        return r
```

[title]: https://leetcode-cn.com/problems/decode-ways
