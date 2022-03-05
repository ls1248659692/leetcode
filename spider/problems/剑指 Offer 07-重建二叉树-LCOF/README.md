# [重建二叉树 LCOF][title]

## Description

输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
            Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]    Output: [3,9,20,null,null,15,7]    

**示例 2:**
            Input: preorder = [-1], inorder = [-1]    Output: [-1]    

**限制：**

`0 <= 节点个数 <= 5000`

**注意** ：本题与主站 105 题重复：<https://leetcode-cn.com/problems/construct-binary-tree-
from-preorder-and-inorder-traversal/>


**Tags:** Tree, Array, Hash Table, Divide and Conquer, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

[title]: https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
