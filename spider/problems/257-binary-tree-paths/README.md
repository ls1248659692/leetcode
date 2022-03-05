# [Binary Tree Paths][title]

## Description

给你一个二叉树的根节点 `root` ，按 **任意顺序** ，返回所有从根节点到叶子节点的路径。

**叶子节点** 是指没有子节点的节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg)
            **输入：** root = [1,2,3,null,5]    **输出：** ["1->2->5","1->3"]    

**示例 2：**
            **输入：** root = [1]    **输出：** ["1"]    



**提示：**

  * 树中节点的数目在范围 `[1, 100]` 内
  * `-100 <= Node.val <= 100`


**Tags:** Tree, Depth-First Search, String, Backtracking, Binary Tree

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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root.left and not root.right: return ['%d'%root.val]
        else:
            res =[]
            if root.left: 
                res.extend(['%d->'%root.val + path for path in  self.binaryTreePaths(root.left)])
            if root.right: 
                res.extend(['%d->'%root.val + path for path in self.binaryTreePaths(root.right)])
            return res
```

[title]: https://leetcode-cn.com/problems/binary-tree-paths
