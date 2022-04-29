# [Binary Tree Preorder Traversal][title]

## Description

给你二叉树的根节点 `root` ，返回它节点值的 **前序** __ 遍历。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)
            **输入：** root = [1,null,2,3]    **输出：** [1,2,3]    

**示例 2：**
            **输入：** root = []    **输出：** []    

**示例 3：**
            **输入：** root = [1]    **输出：** [1]    

**示例 4：**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)
            **输入：** root = [1,2]    **输出：** [1,2]    

**示例 5：**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)
            **输入：** root = [1,null,2]    **输出：** [1,2]    

**提示：**

  * 树中节点数目在范围 `[0, 100]` 内
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def v1(root):
            def pt(nd,nullval):
                if not nd:return nullval
                elif not nd.left and not nd.right: res= [ nd.val]
                else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
                return res
            res= pt(root,[])
            while res and not res[-1]:res.pop()
            return res

        def v2(nd):
            tls,stk=[],[]
            while nd or stk:
                #if nd: tls.append(nd.val)
                while nd : 
                    stk.append(nd)
                    tls.append(nd.val)
                    nd=nd.left
                nd=stk.pop()
                nd=nd.right
            return tls
        return v2(root)
```

[title]: https://leetcode-cn.com/problems/binary-tree-preorder-traversal
