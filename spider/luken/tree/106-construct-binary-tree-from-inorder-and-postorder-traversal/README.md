# [Construct Binary Tree from Inorder and Postorder Traversal][title]

## Description

给定两个整数数组 `inorder` 和 `postorder` ，其中 `inorder` 是二叉树的中序遍历， `postorder`
是同一棵树的后序遍历，请你构造并返回这颗  _二叉树_  。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
            **输入：** inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]    **输出：** [3,9,20,null,null,15,7]    

**示例 2:**
            **输入：** inorder = [-1], postorder = [-1]    **输出：** [-1]    



**提示:**

  * `1 <= inorder.length <= 3000`
  * `postorder.length == inorder.length`
  * `-3000 <= inorder[i], postorder[i] <= 3000`
  * `inorder` 和 `postorder` 都由 **不同** 的值组成
  * `postorder` 中每一个值都在 `inorder` 中
  * `inorder`  **保证** 是树的中序遍历
  * `postorder`  **保证** 是树的后序遍历


**Tags:** Tree, Array, Hash Table, Divide and Conquer, Binary Tree

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def bt(pro,ino):
            if not pro: return None
            elif len(pro)==1: return TreeNode(pro[0])
            else:
                td=TreeNode(pro[-1])
                ln,rootpos = len(pro),ino.index(pro[-1])
                td.left =bt(pro[:rootpos],ino[:rootpos])
                td.right =bt(pro[rootpos:ln-1],ino[rootpos+1:ln])
            return td
        return bt(postorder,inorder)       
```

[title]: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
