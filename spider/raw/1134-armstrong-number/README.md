# [Armstrong Number][title]

## Description

给你一个整数 `n` ，让你来判定他是否是 ** ** **阿姆斯特朗数** ，是则返回 `true`，不是则返回 `false`。

假设存在一个 `k` 位数 `n` ，其每一位上的数字的 `k` 次幂的总和也是 `n` ，那么这个数是阿姆斯特朗数 。



**示例 1：**
            **输入：** n = 153    **输出：** true    **示例：**    153 是一个 3 位数，且 153 = 13 + 53 + 33。    

**示例 2：**
            **输入：** n = 123    **输出：** false    **解释：** 123 是一个 3 位数，且 123 != 13 + 23 + 33 = 36。    



**提示：**

  * `1 <= n <= 108`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        ans = 0
        k = len(s)
        for i in s:
            ans += int(i)**k
        return n == ans

```

[title]: https://leetcode-cn.com/problems/armstrong-number
