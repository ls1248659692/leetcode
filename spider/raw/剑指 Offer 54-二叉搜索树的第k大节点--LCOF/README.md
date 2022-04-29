# [二叉搜索树的第k大节点  LCOF][title]

## Description

给定一棵二叉搜索树，请找出其中第 `k` 大的节点的值。



**示例 1:**
            **输入:** root = [3,1,4,null,2], k = 1       3      / \     1   4      \       2    **输出:** 4

**示例 2:**
            **输入:** root = [5,3,6,2,4,null,null,1], k = 3           5          / \         3   6        / \       2   4      /     1    **输出:** 4



**限制：**

  * 1 ≤ k ≤ 二叉搜索树元素个数


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val]+[dd*unit]]
            else:
                if order=='pre':
                    res= [[nd.val]+[dd]] + trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1)
            return res        
        tli = trs(root,'pre',[None],1)     
        print(tli)
        return sorted([el[0] for el in tli if el[0] is not None])[-k]   
```

[title]: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
