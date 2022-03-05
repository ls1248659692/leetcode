# [Invert Binary Tree][title]

## Description

给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)
            **输入：** root = [4,2,7,1,3,6,9]    **输出：** [4,7,2,9,6,3,1]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)
            **输入：** root = [2,1,3]    **输出：** [2,3,1]    

**示例 3：**
            **输入：** root = []    **输出：** []    



**提示：**

  * 树中节点数目范围在 `[0, 100]` 内
  * `-100 <= Node.val <= 100`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NTreeNode(TreeNode):
    def __init__(self, val=0, left=None, right=None,nleft=None,nright=None):
        super.__init__()
        self.nleft=self.right
        self.nright = self.left

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def trs_v4(nd):
            if not nd:return nd
            elif  not nd.left and not nd.right:return nd
            else:
                n_left = trs_v4(nd.left) if nd.left else None
                n_rigt = trs_v4(nd.right)  if nd.right else None
                if nd.left or nd.right:
                    nd.right,nd.left= n_left,n_rigt
                return nd

        return trs_v4(root)    
```

[title]: https://leetcode-cn.com/problems/invert-binary-tree
