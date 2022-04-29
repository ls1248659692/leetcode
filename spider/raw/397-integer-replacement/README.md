# [Integer Replacement][title]

## Description

给定一个正整数 `n` ，你可以做如下操作：

  1. 如果 `n` _ _ 是偶数，则用 `n / 2`替换 `n` __ 。
  2. 如果 `n` _ _ 是奇数，则可以用 `n + 1`或`n - 1`替换 `n` 。

返回 `n` _ _ 变为 `1` 所需的 _最小替换次数_ 。



**示例 1：**
            **输入：** n = 8    **输出：** 3    **解释：** 8 -> 4 -> 2 -> 1    

**示例 2：**
            **输入：** n = 7    **输出：** 4    **解释：** 7 -> 8 -> 4 -> 2 -> 1    或 7 -> 6 -> 3 -> 2 -> 1    

**示例 3：**
            **输入：** n = 4    **输出：** 2    



**提示：**

  * `1 <= n <= 231 - 1`


**Tags:** Greedy, Bit Manipulation, Memoization, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:return 0
        elif n%2==0: 
            return 1 + self.integerReplacement(n//2)
        else:
            return 2 + min(self.integerReplacement(n//2),self.integerReplacement(n//2+1))
```

[title]: https://leetcode-cn.com/problems/integer-replacement
