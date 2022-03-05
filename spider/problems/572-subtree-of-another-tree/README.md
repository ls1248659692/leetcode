# [Subtree of Another Tree][title]

## Description

给你两棵二叉树 `root` 和 `subRoot` 。检验 `root` 中是否包含和 `subRoot` 具有相同结构和节点值的子树。如果存在，返回
`true` ；否则，返回 `false` 。

二叉树 `tree` 的一棵子树包括 `tree` 的某个节点和这个节点的所有后代节点。`tree` 也可以看做它自身的一棵子树。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)
            **输入：** root = [3,4,5,1,2], subRoot = [4,1,2]    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
            **输入：** root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]    **输出：** false    

**提示：**

  * `root` 树上的节点数量范围是 `[1, 2000]`
  * `subRoot` 树上的节点数量范围是 `[1, 1000]`
  * `-104 <= root.val <= 104`
  * `-104 <= subRoot.val <= 104`


**Tags:** Tree, Depth-First Search, Binary Tree, String Matching, Hash Function

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
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        tli =[]
        val = subRoot.val

        def se(nd):
            if nd.val== val:tli.append(nd)
            if nd.left:se(nd.left)
            if nd.right:se(nd.right)
        se(root)
    

        def pt(nd,nullval):
            if not nd:return nullval
            elif not nd.left and not nd.right: res= [ nd.val]
            else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
            return res
        print(len(tli))
        #return False
        
        for subt in tli[::-1]:
            if pt(subt,[None])==pt(subRoot,[None]):return True
        return False
```

[title]: https://leetcode-cn.com/problems/subtree-of-another-tree
