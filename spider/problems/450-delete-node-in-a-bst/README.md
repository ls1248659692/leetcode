# [Delete Node in a BST][title]

## Description

给定一个二叉搜索树的根节点 **root** 和一个值 **key** ，删除二叉搜索树中的  **key
**对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

  1. 首先找到需要删除的节点；
  2. 如果找到了，删除它。



**示例 1:**

![](https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg)
            **输入：** root = [5,3,6,2,4,null,7], key = 3    **输出：** [5,4,6,2,null,null,7]    **解释：** 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。    一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。    另一个正确答案是 [5,2,6,null,4,null,7]。        ![](https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg)    

**示例 2:**
            **输入:** root = [5,3,6,2,4,null,7], key = 0    **输出:** [5,3,6,2,4,null,7]    **解释:** 二叉树不包含值为 0 的节点    

**示例 3:**
            **输入:** root = [], key = 0    **输出:** []



**提示:**

  * 节点数的范围 `[0, 104]`.
  * `-105 <= Node.val <= 105`
  * 节点值唯一
  * `root` 是合法的二叉搜索树
  * `-105 <= key <= 105`



**进阶：** 要求算法时间复杂度为 O(h)，h 为树的高度。


**Tags:** Tree, Binary Search Tree, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def v1(node,key):
            root,par, match = node,None,False
            while node and node.val!=key:
                
                if key<node.val: par,node=node,node.left
                else: par,node=node,node.right
            if node and key == node.val:match=True
            if not match: return root
            prv,nxn= node.left,node.right
            #node.left,node.right =None,None
            if par is not None:
                cd = 'L' if par.left==node else 'R'
                if nxn is not None:
                    if prv is None:
                        if cd=='R':par.right=nxn
                        if cd=='L':par.left=nxn
                    else:
                        link= prv
                        while link.right: link= link.right
                        link.right =nxn
                        if cd=='R': par.right=prv
                        if cd=='L': par.left=prv
                else:
                    if cd=='R': par.right=prv
                    if cd=='L': par.left=prv
            else:
                if nxn is not None:
                    if  prv is None:
                        return nxn
                    else:
                        lnk = nxn
                        while lnk.left: lnk= lnk.left
                        lnk.left =prv
                        return nxn
                else:
                    return prv                
            return root 

        return v1(root,key) if root else None
```

[title]: https://leetcode-cn.com/problems/delete-node-in-a-bst
