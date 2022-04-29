# [Longest Univalue Path][title]

## Description

给定一个二叉树的 `root` ，返回  _最长的路径的长度_ ，这个路径中的  _每个节点具有相同值_  。 这条路径可以经过也可以不经过根节点。

**两个节点之间的路径长度**  由它们之间的边数表示。



**示例 1:**

![](https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg)
            **输入：** root = [5,4,5,1,1,5]    **输出：** 2    

**示例 2:**

![](https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg)
            **输入：** root = [1,4,5,4,4,5]    **输出：** 2    



**提示:**

  * 树的节点数的范围是 `[0, 104]` 
  * `-1000 <= Node.val <= 1000`
  * 树的深度将不超过 `1000` 


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def iseq(node,pv):
            if not node: r= 0
            elif not node.left and not node.right: r= 1 if node.val==pv else 0
            else: 
                lft,rht=iseq(node.left,node.val),iseq(node.right,node.val)
                r= max(lft , rht)+1 if node.val==pv else 0
                if tli[0]<max(lft+rht,r):tli[0]=max(lft+rht,r)
            if tli[0]<r:tli[0]=r
            return r

        tli=[0]
        iseq(root,None)
        #print(tli)
        return max(tli) if tli else 0
```

[title]: https://leetcode-cn.com/problems/longest-univalue-path
