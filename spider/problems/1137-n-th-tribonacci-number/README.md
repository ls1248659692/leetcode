# [N-th Tribonacci Number][title]

## Description

泰波那契序列 Tn 定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn \+ Tn+1 \+ Tn+2

给你整数 `n`，请返回第 n 个泰波那契数 Tn 的值。



**示例 1：**
            **输入：** n = 4    **输出：** 4    **解释：**    T_3 = 0 + 1 + 1 = 2    T_4 = 1 + 1 + 2 = 4    

**示例 2：**
            **输入：** n = 25    **输出：** 1389537    



**提示：**

  * `0 <= n <= 37`
  * 答案保证是一个 32 位整数，即 `answer <= 2^31 - 1`。


**Tags:** Memoization, Math, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def tribonacci(self, n: int) -> int:
        def v1(n):
            t1,t2,t3=1,1,0
            while n>=3: t1,t2,t3,n =t1+t2+t3,t1,t2, n-1
            return t1 if n>=1 else 0

        def v0(n):
            cache={}
            def tb(n):
                if n in cache:return cache[n]
                if n==0:return 0
                elif n==1:return 1
                elif n==2:return 1
                else:
                    res = tb(n-3)+tb(n-2)+tb(n-1)
                    cache[n]=res
                return res
            return tb(n)
        return v1(n)
```

[title]: https://leetcode-cn.com/problems/n-th-tribonacci-number
