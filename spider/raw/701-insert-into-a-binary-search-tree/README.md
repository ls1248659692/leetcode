# [Insert into a Binary Search Tree][title]

## Description

给定二叉搜索树（BST）的根节点 `root` 和要插入树中的值 `value` ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据
**保证** ，新值和原始二叉搜索树中的任意节点值都不同。

**注意** ，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 **任意有效的结果** 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)
            **输入：** root = [4,2,7,1,3], val = 5    **输出：** [4,2,7,1,3,5]    **解释：** 另一个满足题目要求可以通过的树是：    ![](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)    

**示例 2：**
            **输入：** root = [40,20,60,10,30,50,70], val = 25    **输出：** [40,20,60,10,30,50,70,null,null,25]    

**示例 3：**
            **输入：** root = [4,2,7,1,3,null,null,null,null,null,null], val = 5    **输出：** [4,2,7,1,3,5]    



**提示：**

  * 树中的节点数将在 `[0, 104]`的范围内。
  * `-108 <= Node.val <= 108`
  * 所有值 `Node.val` 是  **独一无二**  的。
  * `-108 <= val <= 108`
  * **保证**  `val` 在原始BST中不存在。


**Tags:** Tree, Binary Search Tree, Binary Tree

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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def it(nd,v):
            nonlocal par,direct
            while nd:
                if v<nd.val: par,direct,nd =nd,'L',nd.left
                else: par,direct,nd= nd,'R',nd.right
            print(nd,par.val)
            if par:
                if direct=='L': 
                    par.left=TreeNode(v)
                if direct=='R': 
                    par.right=TreeNode(v)   
                                 
        par,direct=None,''
        if not root:return TreeNode(val)
        it(root,val)     
        return root

```

[title]: https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
