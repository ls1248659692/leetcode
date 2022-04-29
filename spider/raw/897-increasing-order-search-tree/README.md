# [Increasing Order Search Tree][title]

## Description

给你一棵二叉搜索树的 `root` ，请你 **按中序遍历**
将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg)
            **输入：** root = [5,3,6,2,4,null,8,1,null,null,null,7,9]    **输出：** [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg)
            **输入：** root = [5,1,7]    **输出：** [1,null,5,null,7]    



**提示：**

  * 树中节点数的取值范围是 `[1, 100]`
  * `0 <= Node.val <= 1000`


**Tags:** Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree

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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tli=[]
        def tr(nd):
            if not nd :return [None]
            elif not nd.left and not nd.right: 
                return[nd.val]
            else:
                lf = tr(nd.left)
                rt = tr(nd.right)
                return lf +[nd.val]+rt
        ts = tr(root)
        print(ts)
        nds = [TreeNode(nd) for nd in ts if nd is not None]
        for n in  range(len(nds)-1):
            nds[n].right = nds[n+1]
        return nds[0]


```

[title]: https://leetcode-cn.com/problems/increasing-order-search-tree
