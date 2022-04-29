# [Construct Binary Search Tree from Preorder Traversal][title]

## Description

给定一个整数数组，它表示BST(即 **二叉搜索树** )的 **先** **序遍历** ，构造树并返回其根。

**保证** 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。

**二叉搜索树** 是一棵二叉树，其中每个节点， `Node.left` 的任何后代的值 **严格小于** `Node.val` ,
`Node.right` 的任何后代的值 **严格大于** `Node.val`。

二叉树的 **前序遍历** 首先显示节点的值，然后遍历`Node.left`，最后遍历`Node.right`。



**示例 1：**

![](https://assets.leetcode.com/uploads/2019/03/06/1266.png)
            **输入：** preorder = [8,5,1,7,10,12]    **输出：** [8,5,10,1,7,null,12]    

**示例 2:**
            **输入:** preorder = [1,3]    **输出:** [1,null,3]    



**提示：**

  * `1 <= preorder.length <= 100`
  * `1 <= preorder[i] <= 10^8`
  * `preorder` 中的值 **互不相同**




**Tags:** Stack, Tree, Binary Search Tree, Array, Binary Tree, Monotonic Stack

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
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def bp(l,r):
            if l==r: return None
            if l+1==r: return TreeNode(ls[l])
            for i in range(l,r):
                if ls[i]>ls[l]:break
            if ls[i]<ls[l]:i=r
            print(i,l,r)
            td =TreeNode(ls[l])
            td.left =bp(l+1,i)
            td.right = bp(i,r)
            return td

        ls = preorder
        return bp(0,len(ls))
```

[title]: https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal
