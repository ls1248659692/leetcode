# [Maximum Depth of N-ary Tree][title]

## Description

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
            **输入：** root = [1,null,3,2,4,null,5,6]    **输出：** 3    

**示例 2：**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
            **输入：** root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]    **输出：** 5    

**提示：**

  * 树的深度不会超过 `1000` 。
  * 树的节点数目位于 `[0, 104]` 之间。


**Tags:** Tree, Depth-First Search, Breadth-First Search

**Difficulty:** Easy

## 思路

``` python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        dli =[[]]
        def dp(nd,hr):
            if len(dli)<=hr :dli.append([])
            dli[hr].append(nd.val)
            for ch in nd.children:
                dp(ch,hr+1)

        if not root:return 0
        dp(root,1)
        print(len(dli))
        return len(dli)-1
```

[title]: https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree
