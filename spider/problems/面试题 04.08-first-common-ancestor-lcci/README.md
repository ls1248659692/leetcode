# [First Common Ancestor LCCI][title]

## Description

设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]
                3       / \      5   1     / \ / \    6  2 0  8      / \     7   4    

**示例 1:**
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1    **输出:** 3    **解释:** 节点 5 和节点 1 的最近公共祖先是节点 3。

**示例 2:**
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4    **输出:** 5    **解释:** 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

**说明:**
            所有节点的值都是唯一的。    p、q 为不同节点且均存在于给定的二叉树中。


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order+'-',dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order+'d']+[dd*unit]]
            else:
                res = trs(nd.left,'l',nullv,dd+1) + trs(nd.right,'r',nullv,dd+1) +[[nd.val,order+'t']+[dd]]
            return res        
        tli = trs(root,'o',[None],1) 
        print(tli)
        vli = []
        mindp = 100000
        last_t = None
        for i in range(len(tli)):

            if tli[i][0] in [p.val,q.val]:
                vli.append(list(tli[i]))
            if len(vli)==2:
                if tli[i][-1]< mindp:
                    last_t = list(tli[i])
                    break
            if vli: 
                if mindp> tli[i][-1]: mindp = tli[i][-1]
        #print(vli,last_t)
        val =last_t[0]
        tgli =[]

        def se(nd):
            if tgli:return
            if nd.val== val:tgli.append(nd)
            if nd.left:se(nd.left)
            if nd.right:se(nd.right)
        se(root)        
        return tgli[-1]       
```

[title]: https://leetcode-cn.com/problems/first-common-ancestor-lcci
