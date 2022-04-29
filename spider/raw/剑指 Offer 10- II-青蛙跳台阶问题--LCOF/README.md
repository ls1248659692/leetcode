# [青蛙跳台阶问题  LCOF][title]

## Description

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 `n` 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**
            **输入：** n = 2    **输出：** 2    

**示例 2：**
            **输入：** n = 7    **输出：** 21    

**示例 3：**
            **输入：** n = 0    **输出：** 1

**提示：**

  * `0 <= n <= 100`

注意：本题与主站 70 题相同：<https://leetcode-cn.com/problems/climbing-stairs/>




**Tags:** Memoization, Math, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def numWays(self, n: int) -> int:
        cache={0:1,1:1}
        def cs(n):
            r = 1
            if n in cache: return cache[n]
            if n>1:
                r1 = r*cs(n-1)
                r2 = r*cs(n-2)
                r= r1+r2
            cache[n]=r
            return r %1000000007
        return cs(n)        
```

[title]: https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
