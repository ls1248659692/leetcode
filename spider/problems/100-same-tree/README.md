# [Same Tree][title]

## Description

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)
            **输入：** p = [1,2,3], q = [1,2,3]    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)
            **输入：** p = [1,2], q = [1,null,2]    **输出：** false    

**示例 3：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)
            **输入：** p = [1,2,1], q = [1,1,2]    **输出：** false    

**提示：**

  * 两棵树上的节点数目都在范围 `[0, 100]` 内
  * `-104 <= Node.val <= 104`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def v0(p,q):
            def pt(nd,nullval):
                if not nd:return nullval
                elif not nd.left and not nd.right: res= [ nd.val]
                else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
                return res
            pli = pt(p,[None]) 
            qli =pt(q,[None])
            return pli == qli

        def iseq(p,q):
            return  p==q if None in [p,q] else p.val==q.val and iseq(p.left,q.left) and iseq(p.right,q.right)
        return iseq(p,q)
```

[title]: https://leetcode-cn.com/problems/same-tree
