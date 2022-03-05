# [平衡二叉树 LCOF][title]

## Description

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

**示例 1:**

给定二叉树 `[3,9,20,null,null,15,7]`
                3       / \      9  20        /  \       15   7

返回 `true` 。  
  
**示例 2:**

给定二叉树 `[1,2,2,3,3,null,null,4,4]`
                   1          / \         2   2        / \       3   3      / \     4   4    

返回 `false` 。

**限制：**

  * `0 <= 树的结点个数 <= 10000`

注意：本题与主站 110 题相同：<https://leetcode-cn.com/problems/balanced-binary-tree/>


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

[title]: https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
