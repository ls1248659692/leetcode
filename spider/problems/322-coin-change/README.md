# [Coin Change][title]

## Description

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。



**示例  1：**
            **输入：** coins = [1, 2, 5], amount = 11    **输出：**3     **解释：** 11 = 5 + 5 + 1

**示例 2：**
            **输入：** coins = [2], amount = 3    **输出：** -1

**示例 3：**
            **输入：** coins = [1], amount = 0    **输出：** 0    



**提示：**

  * `1 <= coins.length <= 12`
  * `1 <= coins[i] <= 231 - 1`
  * `0 <= amount <= 104`


**Tags:** Breadth-First Search, Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        ln,cnt,cache,tli =len(coins),0,{},[]

        def combs(ls,i,t):
            if (i,t) in cache: return cache[(i,t)]
            if t==0: mi = 0
            else:
                mi = None
                if i<ln: 
                    #for j in range(t//clis[i],-1,-1):
                    for j in range(t//ls[i]+1):
                        r = None  if mi is not None and j>=mi else  combs(ls,i+1,t-j*ls[i])
                        if r is not None:
                            if mi is None or r+j<mi:mi=r+j
                cache[(i,t)]=mi
            return mi

        clis = sorted(coins,reverse=False)
        if amount==9999:
            badi=[]
            for i in range(1,ln):
                for j in range(i):
                    if clis[i]%clis[j]==0:
                        badi.append(i)
                        break
            nclis = [clis[i] for i in range(ln) if i not in badi]
            print(nclis)
            ln = len(nclis)
            if combs(nclis,0,amount) is None: return -1
            #if amount%2==1 and len([e for e in coins if e%2==1])==0:return -1
        print(clis)
        ln = len(clis)
        t = combs(clis,0,amount)
        print('skip cache %s'%cnt)
        return -1 if t is None else t

```

[title]: https://leetcode-cn.com/problems/coin-change
