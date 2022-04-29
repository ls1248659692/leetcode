# [Merge Two Binary Trees][title]

## Description

给你两棵二叉树： `root1` 和 `root2` 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，
**不为** null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

**注意:** 合并过程必须从两个树的根节点开始。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/05/merge.jpg)
            **输入：** root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]    **输出：** [3,4,5,5,4,null,7]    

**示例 2：**
            **输入：** root1 = [1], root2 = [1,2]    **输出：** [2,2]    



**提示：**

  * 两棵树中的节点数目在范围 `[0, 2000]` 内
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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def mg(r1,r2):
            if not r1 and not r2:return None 
            elif r1 and not r2: return r1
            elif not r1 and r2: return r2
            else:
                r1.val +=r2.val
                r1.left=mg(r1.left,r2.left)
                r1.right=mg(r1.right,r2.right)
                return r1
            print(r1,r2)
        res = mg(root1,root2)
        return res

```

[title]: https://leetcode-cn.com/problems/merge-two-binary-trees
