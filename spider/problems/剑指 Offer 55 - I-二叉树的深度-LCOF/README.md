# [二叉树的深度 LCOF][title]

## Description

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 `[3,9,20,null,null,15,7]`，
                3       / \      9  20        /  \       15   7

返回它的最大深度 3 。



**提示：**

  1. `节点总数 <= 10000`

注意：本题与主站 104 题相同：<https://leetcode-cn.com/problems/maximum-depth-of-binary-
tree/>


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
    def maxDepth(self, root: TreeNode) -> int:
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val]+[dd*100000]]
            else:
                if order=='pre':
                    res= [[nd.val]+[dd]] + trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1)
                if order=='pos':
                    res = trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1) +[[nd.val]+[dd]]
            return res        
        tli = trs(root,'pre',[None],1)
        #print(tli)
        return max(el[1]//100000 for el in tli if el[1]>=100000) if root else 0        
```

[title]: https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
