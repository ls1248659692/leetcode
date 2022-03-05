# [Construct Binary Tree from Preorder and Inorder Traversal][title]

## Description

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的 **先序遍历** ， `inorder`
是同一棵树的 **中序遍历** ，请构造二叉树并返回其根节点。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
            **输入** **:** preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]    **输出:** [3,9,20,null,null,15,7]    

**示例 2:**
            **输入:** preorder = [-1], inorder = [-1]    **输出:** [-1]    



**提示:**

  * `1 <= preorder.length <= 3000`
  * `inorder.length == preorder.length`
  * `-3000 <= preorder[i], inorder[i] <= 3000`
  * `preorder` 和 `inorder` 均 **无重复** 元素
  * `inorder` 均出现在 `preorder`
  * `preorder`  **保证** 为二叉树的前序遍历序列
  * `inorder`  **保证** 为二叉树的中序遍历序列


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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def bt(pro,ino):
            if not pro: return None
            elif len(pro)==1: return TreeNode(pro[0])
            else:
                td=TreeNode(pro[0])
                rootpos = ino.index(pro[0])
                td.left =bt(pro[1:rootpos+1],ino[:rootpos])
                td.right =bt(pro[rootpos+1:],ino[rootpos+1:])
            return td
        pro,ino= preorder,inorder
        return bt(preorder,inorder)
    
            
```

[title]: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
