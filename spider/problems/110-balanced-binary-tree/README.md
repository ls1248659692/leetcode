# [Balanced Binary Tree][title]

## Description

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

> 一个二叉树 _每个节点_ 的左右两个子树的高度差的绝对值不超过 1 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)
            **输入：** root = [3,9,20,null,null,15,7]    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)
            **输入：** root = [1,2,2,3,3,null,null,4,4]    **输出：** false    

**示例 3：**
            **输入：** root = []    **输出：** true    

**提示：**

  * 树中的节点数在范围 `[0, 5000]` 内
  * `-104 <= Node.val <= 104`


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
    def isBalanced(self, root: TreeNode) -> bool:
        ut= 1
        def trs_v3(nd,nullv,dd):
            if not nd:return [nullv+[0,0]]
            elif not nd.left and not nd.right: res= [[nd.val]+[1,1]] 
            else:
                left = trs_v3(nd.left,nullv,dd)
                rigt = trs_v3(nd.right,nullv,dd)
                res = left + rigt + [[nd.val]+[max(left[-1][1:])+1,max(rigt[-1][1:])+1]] 
            return res        
        if not root: return True
        
        tli = trs_v3(root,[None],1)
        print (tli)
        return True if sum(abs(el[1]-el[2])>1 for el in tli)==0 else False   
```

[title]: https://leetcode-cn.com/problems/balanced-binary-tree
