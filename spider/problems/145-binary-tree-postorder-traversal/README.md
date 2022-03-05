# [Binary Tree Postorder Traversal][title]

## Description

给你一棵二叉树的根节点 `root` ，返回其节点值的 **后序遍历** 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg)
            **输入：** root = [1,null,2,3]    **输出：** [3,2,1]    

**示例 2：**
            **输入：** root = []    **输出：** []    

**示例 3：**
            **输入：** root = [1]    **输出：** [1]    



**提示：**

  * 树中节点的数目在范围 `[0, 100]` 内
  * `-100 <= Node.val <= 100`



**进阶：** 递归算法很简单，你可以通过迭代算法完成吗？


**Tags:** Stack, Tree, Depth-First Search, Binary Tree

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def trs(nd,order,nullv):
            if not nd:return nullv
            elif not nd.left and not nd.right: res= [ nd.val]
            else:
                if order=='pre':
                    res= [nd.val] + trs(nd.left,order,nullv) + trs(nd.right,order,nullv)
                if order=='pos':
                    res = trs(nd.left,order,nullv) + trs(nd.right,order,nullv) +[nd.val] 
            return res
        return trs(root,'pos',[])
```

[title]: https://leetcode-cn.com/problems/binary-tree-postorder-traversal
