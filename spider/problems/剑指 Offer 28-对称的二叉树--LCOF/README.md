# [对称的二叉树  LCOF][title]

## Description

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

`    1  
   / \  
  2   2  
 / \ / \  
3  4 4  3`  
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

`    1  
   / \  
  2   2  
   \   \  
   3    3`



**示例 1：**
            **输入：** root = [1,2,2,3,4,4,3]    **输出：** true    

**示例 2：**
            **输入：** root = [1,2,2,null,3,null,3]    **输出：** false



**限制：**

`0 <= 节点个数 <= 1000`

注意：本题与主站 101 题相同：<https://leetcode-cn.com/problems/symmetric-tree/>


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def trs_v4(nd):
            if not nd:return nd
            elif  not nd.left and not nd.right:return nd
            else:
                n_left = trs_v4(nd.left) if nd.left else None
                n_rigt = trs_v4(nd.right)  if nd.right else None
                if nd.left or nd.right:
                    nd.right,nd.left= n_left,n_rigt
                return nd
        def pt(nd,nullval):
            if not nd:return nullval
            elif not nd.left and not nd.right: res= [ nd.val]
            else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
            return res
        rli = pt(root,['None'])
        tr= trs_v4(root) 
        print('root=%s
..tr=%s'%(root,tr))
        return rli == pt(tr,['None'])
```

[title]: https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
