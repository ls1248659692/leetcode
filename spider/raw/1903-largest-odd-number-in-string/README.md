# [Largest Odd Number in String][title]

## Description

给你一个字符串 `num` ，表示一个大整数。请你在字符串 `num` 的所有 **非空子字符串** 中找出 **值最大的奇数**
，并以字符串形式返回。如果不存在奇数，则返回一个空字符串 __`""` __ 。

**子字符串** 是字符串中的一个连续的字符序列。

**示例 1：**
            **输入：** num = "52"    **输出：** "5"    **解释：** 非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。    

**示例 2：**
            **输入：** num = "4206"    **输出：** ""    **解释：** 在 "4206" 中不存在奇数。    

**示例 3：**
            **输入：** num = "35427"    **输出：** "35427"    **解释：** "35427" 本身就是一个奇数。    

**提示：**

  * `1 <= num.length <= 105`
  * `num` 仅由数字组成且不含前导零


**Tags:** Greedy, Math, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 == 1:
                return num[:i+1]
        return ''
```

[title]: https://leetcode-cn.com/problems/largest-odd-number-in-string
