# [Leaf-Similar Trees][title]

## Description

请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个  **叶值序列** 。

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

举个例子，如上图所示，给定一棵叶值序列为 `(6, 7, 4, 9, 8)` 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是  _叶相似  _的。

如果给定的两个根结点分别为 `root1` 和 `root2` 的树是叶相似的，则返回 `true`；否则返回 `false` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)
            **输入：** root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)
            **输入：** root1 = [1,2,3], root2 = [1,3,2]    **输出：** false    



**提示：**

  * 给定的两棵树结点数在 `[1, 200]` 范围内
  * 给定的两棵树上的值在 `[0, 200]` 范围内


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tli =[]
        def tr(nd):
            if not nd:return 
            if not nd.left and not nd.right: tli.append(nd.val)
            tr(nd.left)
            tr(nd.right)
        tr(root1)
        t1 = list(tli)
        tli=[]
        tr(root2)
        t2 = list(tli)
        print('t1=%s,t2=%s'%(t1,t2))
        return  t1==t2
```

[title]: https://leetcode-cn.com/problems/leaf-similar-trees
