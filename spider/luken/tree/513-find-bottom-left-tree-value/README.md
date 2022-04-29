# [Find Bottom Left Tree Value][title]

## Description

给定一个二叉树的 **根节点** `root`，请找出该二叉树的 **最底层 最左边** 节点的值。

假设二叉树中至少有一个节点。

**示例 1:**

![](https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg)
            **输入:** root = [2,1,3]    **输出:** 1    

**示例 2:**

![](https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg)****
            **输入:** [1,2,3,4,null,5,6,null,null,7]    **输出:** 7    

**提示:**

  * 二叉树的节点个数的范围是 `[1,104]`
  * `-231 <= Node.val <= 231 - 1`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def v1(node):
            res,que=[[node.val]],[[node,1]]
            while que:
                node,h =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(node.left.val)
                    que.append([node.left,h+1])
                if node.right:
                    res[h].append(node.right.val)
                    que.append([node.right,h+1])  
            print(res[:-1])
            return res[:-1]  

        return v1(root)[-1][0]         
```

[title]: https://leetcode-cn.com/problems/find-bottom-left-tree-value
