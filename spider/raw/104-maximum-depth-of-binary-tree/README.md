# [Maximum Depth of Binary Tree][title]

## Description

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

**说明:**  叶子节点是指没有子节点的节点。

**示例：**  
给定二叉树 `[3,9,20,null,null,15,7]`，
                3       / \      9  20        /  \       15   7

返回它的最大深度 3 。


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        else:
            mxd=1
            if not root.left and not root.right:
                return 1
            else:
                mxd += max(self.maxDepth(root.left) if root.left else 0 ,self.maxDepth(root.right )if root.right else 0)
            return mxd
```

[title]: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
