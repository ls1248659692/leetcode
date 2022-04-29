# [Search in a Binary Search Tree][title]

## Description

给定二叉搜索树（BST）的根节点 `root` 和一个整数值 `val`。

你需要在 BST 中找到节点值等于 `val` 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 `null` 。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)
            **输入：** root = [4,2,7,1,3], val = 2    **输出：** [2,1,3]    

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)
            **输入：** root = [4,2,7,1,3], val = 5    **输出：** []    



**提示：**

  * 数中节点数在 `[1, 5000]` 范围内
  * `1 <= Node.val <= 107`
  * `root` 是二叉搜索树
  * `1 <= val <= 107`


**Tags:** Tree, Binary Search Tree, Binary Tree

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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        tli =[]
        def sh(nd,val):
            #print(nd.val,tli)
            if tli:return
            if nd.val == val:tli.append(nd)
            if nd.left: sh(nd.left,val)
            if nd.right: sh(nd.right,val)
        sh(root,val)
        return tli[-1] if tli else None
```

[title]: https://leetcode-cn.com/problems/search-in-a-binary-search-tree
