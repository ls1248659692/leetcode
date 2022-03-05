# [Successor LCCI][title]

## Description

设计一个算法，找出二叉搜索树中指定节点的"下一个"节点（也即中序后继）。

如果指定节点没有对应的"下一个"节点，则返回`null`。

**示例 1:**
            **输入:** root = [2,1,3], p = 1          2     / \    1   3        **输出:** 2

**示例 2:**
            **输入:** root = [5,3,6,2,4,null,null,1], p = 6              5         / \        3   6       / \      2   4     /       1        **输出:** null


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        def se(nd,p):
            stk=[]
            while nd or stk:
                #print(nd.val)
                if nd.val==p.val:
                    #print ([e.val for e in stk])
                    if nd.right:
                        q = nd.right
                        while q.left: q =q.left
                        return q
                    while stk:
                        t= stk.pop()
                        return t
                        if t.right:return t.right
                    return None
                elif nd.val >p.val: 
                    stk.append(nd)
                    nd= nd.left
                elif nd.val<p.val:
                    nd =nd.right
        return se(root,p)
```

[title]: https://leetcode-cn.com/problems/successor-lcci
