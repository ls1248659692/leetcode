# [Number of Different Integers in a String][title]

## Description

给你一个字符串 `word` ，该字符串由数字和小写英文字母组成。

请你用空格替换每个不是数字的字符。例如，`"a123bc34d8ef34"` 将会变成 `" 123 34 8 34"`
。注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）：`"123"`、`"34"`、`"8"` 和 `"34"` 。

返回对 `word` 完成替换后形成的 **不同** 整数的数目。

只有当两个整数的 **不含前导零** 的十进制表示不同， 才认为这两个整数也不同。

**示例 1：**
            **输入：** word = "a **123** bc **34** d **8** ef **34** "    **输出：** 3    **解释：** 不同的整数有 "123"、"34" 和 "8" 。注意，"34" 只计数一次。    

**示例 2：**
            **输入：** word = "leet **1234** code **234** "    **输出：** 2    

**示例 3：**
            **输入：** word = "a **1** b **01** c **001** "    **输出：** 1    **解释：** "1"、"01" 和 "001" 视为同一个整数的十进制表示，因为在比较十进制值时会忽略前导零的存在。    

**提示：**

  * `1 <= word.length <= 1000`
  * `word` 由数字和小写英文字母组成


**Tags:** Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tli =['']
        for ch in word:
            if not 0<=ord(ch)-ord('a')<26:
                tli[-1] += ch
            else:
                tli.append('')
        r = set([int(el) for el in tli if el])
        #print (r)

        return len(r)
```

[title]: https://leetcode-cn.com/problems/number-of-different-integers-in-a-string
