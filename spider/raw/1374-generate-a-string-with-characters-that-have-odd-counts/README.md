# [Generate a String With Characters That Have Odd Counts][title]

## Description

给你一个整数 `n`，请你返回一个含 _`n` _个字符的字符串，其中每种字符在该字符串中都恰好出现 **奇数次** _**。**_

返回的字符串必须只含小写英文字母。如果存在多个满足题目要求的字符串，则返回其中任意一个即可。



**示例 1：**
            **输入：** n = 4    **输出：** "pppz"    **解释：** "pppz" 是一个满足题目要求的字符串，因为 'p' 出现 3 次，且 'z' 出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ohhh" 和 "love"。    

**示例 2：**
            **输入：** n = 2    **输出：** "xy"    **解释：** "xy" 是一个满足题目要求的字符串，因为 'x' 和 'y' 各出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ag" 和 "ur"。    

**示例 3：**
            **输入：** n = 7    **输出：** "holasss"    



**提示：**

  * `1 <= n <= 500`


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' if n==1 else 'a'+'b'*(n-1) if n%2==0 else 'ab'+'c'*(n-2)
```

[title]: https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts
