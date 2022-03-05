# [Three Steps Problem LCCI][title]

## Description

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

**示例1:**
            **输入** ：n = 3     **输出** ：4    **说明** : 有四种走法    

**示例2:**
            **输入** ：n = 5    **输出** ：13    

**提示:**

  1. n范围在[1, 1000000]之间


**Tags:** Memoization, Math, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 2:
            return 1
        a = 1
        b = 1
        c = 2
        for _ in range(3,n+1):
            a,b,c = b, c, (a+b+c) %1000000007
        return c
```

[title]: https://leetcode-cn.com/problems/three-steps-problem-lcci
