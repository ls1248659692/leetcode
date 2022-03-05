# [Perfect Squares][title]

## Description

给你一个整数 `n` ，返回 _和为`n` 的完全平方数的最少数量_ 。

**完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，`1`、`4`、`9` 和 `16` 都是完全平方数，而
`3` 和 `11` 不是。



**示例  1：**
            **输入：** n = 12    **输出：** 3     **解释：**12 = 4 + 4 + 4

**示例 2：**
            **输入：** n = 13    **输出：** 2    **解释：**13 = 4 + 9



**提示：**

  * `1 <= n <= 104`


**Tags:** Breadth-First Search, Math, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def numSquares(self, n: int) -> int:
        def v1(n):
            nums,amount = [i*i for i in range(1,101) if i*i<=n],n
            # d={xx:xx//x for x in nums for xx in range(x,n+1,x)}
            ln,cache,c1,c2,mils =len(nums),{},0,0,[n]

            def combs(i,t,s):
                #if (i,t) in cache: return cache[(i,t)]
                #if cache.get(t,[-1,n])[0]>=i: return cache[t][1]
                # if cache.get(t,[n,n])[0]<=i: return cache[t][1]
                if t in cache: return cache[t]
                if s>=mils[-1]:return n
                else:
                    mi = n
                    if i<ln: 
                        for j in range(0,t//cnu[i]+1): 
                            if s+j>mils[-1]:break
                            p=j*cnu[i]
                            if t-p==0:
                                if j<mi:mi=j
                            elif t-p<0:break
                            else:
                                r = n  if j>=mi else  combs(i+1,t-p,s+j)
                                if  r+j<mi:mi=r+j
                    if t==n and mi<mils[-1]: mils.append(mi)
                    #cache[(i,t)]=mi
                    # cache[t]=(i,mi)
                    cache[t]=mi
                return mi


            cnu = sorted(nums,reverse=False)
            if n==1:return 1
            return combs(0,amount,0)
        #for n in range(9999,9998,-1):
        return v1(n)

```

[title]: https://leetcode-cn.com/problems/perfect-squares
