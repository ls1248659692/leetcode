# [Pow(x, n)][title]

## Description

实现 [pow( _x_ , _n_ )](https://www.cplusplus.com/reference/valarray/pow/) ，即计算
`x` 的 `n` 次幂函数（即，`xn` ）。



**示例 1：**
            **输入：** x = 2.00000, n = 10    **输出：** 1024.00000    

**示例 2：**
            **输入：** x = 2.10000, n = 3    **输出：** 9.26100    

**示例 3：**
            **输入：** x = 2.00000, n = -2    **输出：** 0.25000    **解释：** 2-2 = 1/22 = 1/4 = 0.25    



**提示：**

  * `-100.0 < x < 100.0`
  * `-231 <= n <= 231-1`
  * `-104 <= xn <= 104`


**Tags:** Recursion, Math

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    import math
    def myPow(self, x: float, n: int) -> float:
        cache={}
        
        def mp2(n):
            if n in cache:return cache[n]
            if n==1: r= x
            else: r= mp2(n//2)*mp2(n//2)
            cache[n]=r
            return r
                
        def mp(n):
            if n==0:return 1
            if n==1:return x
            else:            
                m2= int(math.log2(n))
                n1= n-2**m2
                return mp2(2**m2)*mp(n1)
            
        return mp(abs(n)) if n>=0 else 1/mp(abs(n))
```

[title]: https://leetcode-cn.com/problems/powx-n
