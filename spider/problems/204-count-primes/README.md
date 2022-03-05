# [Count Primes][title]

## Description

给定整数 `n` ，返回 _所有小于非负整数  `n` 的质数的数量_ 。



**示例 1：**
            **输入：** n = 10    **输出：** 4    **解释：** 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。    

**示例 2：**
            **输入：** n = 0    **输出：** 0    

**示例 3：**
            **输入：** n = 1    **输出** ：0    



**提示：**

  * `0 <= n <= 5 * 106`


**Tags:** Array, Math, Enumeration, Number Theory

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def countPrimes(self, n: int) -> int:
        pli = [ 2,3,5,7]
        cn =4
        for i in range(9,3000,2):
            sq = int(i**0.5)+1
            for p in pli:
                if p >sq:
                    cn+=1
                    pli.append(i)
                    break
                if i%p==0:
                    break
        p3k=list(pli)
        if n<=3000: return len([e for e in p3k if e<n])
        if n>400*1000*1000: return -1
        dic_p = {k:1 for k in range(3001,n)}
        for i in range(len(p3k)):
            for j in range(2,n//p3k[i]+1):
                dic_p[j*p3k[i]]=0
        cn = len(p3k) + len([e for e in dic_p.values() if e==1] )
        return cn
        
```

[title]: https://leetcode-cn.com/problems/count-primes
