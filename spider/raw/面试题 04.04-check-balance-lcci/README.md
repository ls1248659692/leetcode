# [Check Balance LCCI][title]

## Description

实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。

  
 **示例 1:**
            给定二叉树 [3,9,20,null,null,15,7]          3         / \        9  20          /  \         15   7      返回 true 。

 **示例 2:**  
            给定二叉树 [1,2,2,3,3,null,null,4,4]            1           / \          2   2         / \        3   3       / \      4   4      返回 false 。


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root.left and not root.right: res=[(1,0,root.val)]
            else: 
                dlf = depth(root.left) if root.left else [(0,0,None)]
                drg = depth(root.right)if root.right else [(0,0,None)]
                res = dlf+drg+[(max(dlf[-1][0],drg[-1][0])+1,max(dlf[-1][0],drg[-1][0])-min(dlf[-1][0],drg[-1][0]),root.val)]
            return res
        if not root:return True
        dli = depth(root)
        # print(dli)
        return max(e[1]for e in dli)<=1        
```

[title]: https://leetcode-cn.com/problems/check-balance-lcci
