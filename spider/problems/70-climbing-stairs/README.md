# [Climbing Stairs][title]

## Description

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？



**示例 1：**
            **输入：** n = 2    **输出：** 2    **解释：** 有两种方法可以爬到楼顶。    1. 1 阶 + 1 阶    2. 2 阶

**示例 2：**
            **输入：** n = 3    **输出：** 3    **解释：** 有三种方法可以爬到楼顶。    1. 1 阶 + 1 阶 + 1 阶    2. 1 阶 + 2 阶    3. 2 阶 + 1 阶    



**提示：**

  * `1 <= n <= 45`


**Tags:** Memoization, Math, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:

    def climbStairs(self, n: int) -> int:
        cache={0:1,1:1}
        def cs(n):
            r = 1
            if n in cache: return cache[n]
            if n>1:
                r1 = r*cs(n-1)
                r2 = r*cs(n-2)
                r= r1+r2
            cache[n]=r
            return r
        return cs(n)
```

[title]: https://leetcode-cn.com/problems/climbing-stairs
