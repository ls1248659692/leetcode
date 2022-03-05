# [Count Square Sum Triples][title]

## Description

一个 **平方和三元组** `(a,b,c)` 指的是满足 `a2 + b2 = c2` 的 **整数** 三元组 `a`，`b` 和 `c` 。

给你一个整数 `n` ，请你返回满足 __`1 <= a, b, c <= n` 的 **平方和三元组** 的数目。

**示例 1：**
            **输入：** n = 5    **输出：** 2    **解释：** 平方和三元组为 (3,4,5) 和 (4,3,5) 。    

**示例 2：**
            **输入：** n = 10    **输出：** 4    **解释：** 平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。    

**提示：**

  * `1 <= n <= 250`


**Tags:** Math, Enumeration

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countTriples(self, n: int) -> int:
        res=[]
        for i in range(1,n+1-2):
            for j in range(i+1,n+1-1):
                if (i**2 +j**2)**0.5 == int((i**2 +j**2)**0.5) and int((i**2 +j**2)**0.5)<=n:
                    res.append((i,j,int((i**2 +j**2)**0.5)))
                    res.append((j,i,int((i**2 +j**2)**0.5)))
        print (len(res))
        return (len(res))
```

[title]: https://leetcode-cn.com/problems/count-square-sum-triples
