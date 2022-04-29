# [Prime Arrangements][title]

## Description

请你帮忙给从 `1` 到 `n` 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

由于答案可能会很大，所以请你返回答案 **模 mod  `10^9 + 7`** 之后的结果即可。



**示例 1：**
            **输入：** n = 5    **输出：** 12    **解释：** 举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。    

**示例 2：**
            **输入：** n = 100    **输出：** 682289015    



**提示：**

  * `1 <= n <= 100`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_num = 0
        prime_com = 1
        non_com = 1
        nli=[2,3,5,7,11,13,]
        nli=[]
        for i in range(2,n+1):
            isp=True
            for j in range(2,int(n**0.5)+1):
                if i%j==0 and i!=j:
                    isp=False
            if isp:nli.append(i)
        prime_num=len(nli)
        print(nli)

        ex_num = n - prime_num
        for i in range(1,prime_num+1):
            prime_com = prime_com * i
        for j in range(1,ex_num +1):
            non_com = non_com * j
        return (non_com * prime_com)%(10**9 +7)
```

[title]: https://leetcode-cn.com/problems/prime-arrangements
