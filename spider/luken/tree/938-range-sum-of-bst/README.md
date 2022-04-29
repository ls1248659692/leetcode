# [Range Sum of BST][title]

## Description

给定二叉搜索树的根结点 `root`，返回值位于范围 _`[low, high]`_ 之间的所有结点的值的和。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)
            **输入：** root = [10,5,15,3,7,null,18], low = 7, high = 15    **输出：** 32    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg)
            **输入：** root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10    **输出：** 23    

**提示：**

  * 树中节点数目在范围 `[1, 2 * 104]` 内
  * `1 <= Node.val <= 105`
  * `1 <= low <= high <= 105`
  * 所有 `Node.val` **互不相同**


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

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
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        tli =[]
        def sh(nd):
            #print(nd.val,tli)
            if low<=nd.val<=high:tli.append(nd.val)
            if nd.left: sh(nd.left)
            if nd.right: sh(nd.right)
        sh(root)
        return sum(tli) if tli else 0       
```

[title]: https://leetcode-cn.com/problems/range-sum-of-bst
