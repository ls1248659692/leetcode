# [开幕式焰火][title]

## Description

「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。 给定一棵二叉树 `root`
代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。 **示例 1：** >输入：`root =
[1,3,2,1,null,2]` > >输出：`3` > >解释：焰火中有 3 个不同的颜色，值分别为 1、2、3 **示例 2：** >输入：`root
= [3,3,3]` > >输出：`1` > >解释：焰火中仅出现 1 个颜色，值为 3 **提示：** \- `1 <= 节点个数 <= 1000` \-
`1 <= Node.val <= 1000`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree

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
    def numColor(self, root: TreeNode) -> int:
        def pt(nd,nullval):
            if not nd:return nullval
            elif not nd.left and not nd.right: res= [ nd.val]
            else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
            return res
        res= pt(root,[])
        return len(set([e for e in res if e is not None]))        
```

[title]: https://leetcode-cn.com/problems/sZ59z6
