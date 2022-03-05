# [Find Kth Bit in Nth Binary String][title]

## Description

给你两个正整数 `n` 和 `k`，二进制字符串 `Sn` 的形成规则如下：

  * `S1 = "0"`
  * 当 `i > 1` 时，`Si = Si-1 + "1" + reverse(invert(Si-1))`

其中 `+` 表示串联操作，`reverse(x)` 返回反转 `x` 后得到的字符串，而 `invert(x)` 则会翻转 x 中的每一位（0 变为
1，而 1 变为 0）。

例如，符合上述描述的序列的前 4 个字符串依次是：

  * `S1 = "0"`
  * `S2 = "0 **1** 1"`
  * `S3 = "011 **1** 001"`
  * `S4 = "0111001 **1** 0110001"`

请你返回 `Sn` 的 **第`k` 位字符** ，题目数据保证 `k` 一定在 `Sn` 长度范围以内。

**示例 1：**
            **输入：** n = 3, k = 1    **输出：** "0"    **解释：** S3 为 " **0** 111001"，其第 1 位为 "0" 。    

**示例 2：**
            **输入：** n = 4, k = 11    **输出：** "1"    **解释：** S4 为 "0111001101 **1** 0001"，其第 11 位为 "1" 。    

**示例 3：**
            **输入：** n = 1, k = 1    **输出：** "0"    

**示例 4：**
            **输入：** n = 2, k = 3    **输出：** "1"    

**提示：**

  * `1 <= n <= 20`
  * `1 <= k <= 2n - 1`


**Tags:** Recursion, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def  v0(n,k):
            if n == 1: return '0'
            s = '0'
            for i in range(1, n):
                s +=  '1' + s.replace('0','F').replace('1','0').replace('F','1')[::-1]
            return s[k-1]

        def v1(n,k):
            if n == 1:return '0'
            mid = 2**(n-1)
            if k == mid:
                return '1'
            if k < mid:
                return v1(n-1,k)
            elif k > mid:
                k = mid*2 - k
                return '0' if v1(n-1,k) == '1' else '1'
        return v0(n,k)
```

[title]: https://leetcode-cn.com/problems/find-kth-bit-in-nth-binary-string
