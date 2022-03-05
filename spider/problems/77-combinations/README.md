# [Combinations][title]

## Description

给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。

你可以按 **任何顺序** 返回答案。

**示例 1：**
            **输入：** n = 4, k = 2    **输出：**    [      [2,4],      [3,4],      [2,3],      [1,2],      [1,3],      [1,4],    ]

**示例 2：**
            **输入：** n = 1, k = 1    **输出：** [[1]]

**提示：**

  * `1 <= n <= 20`
  * `1 <= k <= n`


**Tags:** Array, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def cmb(n,k):
            if k==0 or len(n)==0: return [[]]
            s0= cmb(n[1:],k)
            s1= [[n[0]]+e for e in cmb(n[1:],k-1)]
            return [e for e in s0+s1 if len(e)==k]
        r= cmb([e for e in range(1,n+1)],k) 
        return [e for e in r if len(e)==k]   
```

[title]: https://leetcode-cn.com/problems/combinations
