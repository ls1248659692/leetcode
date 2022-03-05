# [Flip Equivalent Binary Trees][title]

## Description

我们可以为二叉树 **T** 定义一个  **翻转操作  **，如下所示：选择任意节点，然后交换它的左子树和右子树。

只要经过一定次数的翻转操作后，能使 **X** 等于 **Y** ，我们就称二叉树 **X** _翻转 等价  _于二叉树 **Y** 。

这些树由根节点 `root1` 和 `root2` 给出。如果两个二叉树是否是 _翻转 等价  _的函数，则返回 `true` ，否则返回 `false`
。



**示例 1：**

![Flipped Trees
Diagram](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)
            **输入：** root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]    **输出：** true    **解释：** 我们翻转值为 1，3 以及 5 的三个节点。    

**示例  2:**
            **输入:** root1 = [], root2 = []    **输出:** true    

**示例 3:**
            **输入:** root1 = [], root2 = [1]    **输出:** false    



**提示：**

  * 每棵树节点数在 `[0, 100]` 范围内
  * 每棵树中的每个值都是唯一的、在 `[0, 99]` 范围内的整数


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def eq( r1,r2):
            if None in (r1,r2): return r1==r2
            if r1.val!=r2.val:return False
            return (eq(r1.left,r2.left) and eq(r1.right,r2.right)) or (eq(r1.left,r2.right) and eq(r1.right,r2.left))

        return eq(root1,root2) 
```

[title]: https://leetcode-cn.com/problems/flip-equivalent-binary-trees
