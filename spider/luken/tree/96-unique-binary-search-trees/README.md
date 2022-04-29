# [Unique Binary Search Trees][title]

## Description

给你一个整数 `n` ，求恰由 `n` 个节点组成且节点值从 `1` 到 `n` 互不相同的 **二叉搜索树** 有多少种？返回满足题意的二叉搜索树的种数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)
            **输入：** n = 3    **输出：** 5    

**示例 2：**
            **输入：** n = 1    **输出：** 1    

**提示：**

  * `1 <= n <= 19`


**Tags:** Tree, Binary Search Tree, Math, Dynamic Programming, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def numTrees(self, n: int) -> int:
            # if n==1:return 1
            # if n==2: return 2
            # elif n=3: return ct(2)+ct(1)*ct(1)+ct(2)
            # elif n==4: return ct(3)+ct(2)*ct(1) +ct(1)*ct(2) ct(3)
        c=[1,1,2,5]
        for nn in range(4,n+1):
            c.append(sum(c[j]*c[nn-1-j] for j in range(0,nn)))
        return c[n]

```

[title]: https://leetcode-cn.com/problems/unique-binary-search-trees
