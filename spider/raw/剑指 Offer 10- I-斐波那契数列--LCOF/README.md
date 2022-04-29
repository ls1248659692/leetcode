# [斐波那契数列  LCOF][title]

## Description

写一个函数，输入 `n` ，求斐波那契（Fibonacci）数列的第 `n` 项（即 `F(N)`）。斐波那契数列的定义如下：
            F(0) = 0,   F(1) = 1    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**
            **输入：** n = 2    **输出：** 1    

**示例 2：**
            **输入：** n = 5    **输出：** 5    

**提示：**

  * `0 <= n <= 100`


**Tags:** Memoization, Math, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def fib(self, n: int) -> int:
        def v1(n):
            f1,f2=0, 1
            for i in range(n):f1,f2 = f2,f1+f2
            return f1 % 1000000007
                
        def v0(n):
            cache={0:0,1:1}
            def myfib(n):
                if n in cache:return cache[n]
                if n==0: return 0
                elif n==1:return 1
                else: 
                    r= (myfib(n-1)+myfib(n-2))%(1000000007)
                    cache[n]=r
                    return r
            return myfib(n)
        return v1(n)
```

[title]: https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
