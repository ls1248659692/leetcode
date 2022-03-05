# [Binary Number with Alternating Bits][title]

## Description

给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。



**示例 1：**
            **输入：** n = 5    **输出：** true    **解释：** 5 的二进制表示是：101    

**示例 2：**
            **输入：** n = 7    **输出：** false    **解释：** 7 的二进制表示是：111.

**示例 3：**
            **输入：** n = 11    **输出：** false    **解释：** 11 的二进制表示是：1011.



**提示：**

  * `1 <= n <= 231 - 1`


**Tags:** Bit Manipulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bs = str(bin(n))[2:]
        return not [i for i in range(1,len(bs)) if bs[i]==bs[i-1]]
```

[title]: https://leetcode-cn.com/problems/binary-number-with-alternating-bits
