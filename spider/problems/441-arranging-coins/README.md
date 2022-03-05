# [Arranging Coins][title]

## Description

你总共有 `n` _ _ 枚硬币，并计划将它们按阶梯状排列。对于一个由 `k` 行组成的阶梯，其第 `i` __ 行必须正好有 `i` __
枚硬币。阶梯的最后一行 **可能** 是不完整的。

给你一个数字 `n` __ ，计算并返回可形成 **完整阶梯行** 的总行数。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg)
            **输入：** n = 5    **输出：** 2    **解释：** 因为第三行不完整，所以返回 2 。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg)
            **输入：** n = 8    **输出：** 3    **解释：** 因为第四行不完整，所以返回 3 。    



**提示：**

  * `1 <= n <= 231 - 1`


**Tags:** Math, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def arrangeCoins(self, n: int) -> int:
        for k in range(1,2**31):
            if k*(k+1)//2>n:return k-1

        #(1+k)*k/2<=n <(2+k)*(k+1)/2
```

[title]: https://leetcode-cn.com/problems/arranging-coins
