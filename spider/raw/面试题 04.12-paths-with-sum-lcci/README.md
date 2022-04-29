# [Paths with Sum LCCI][title]

## Description

给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

**示例:**  
给定如下二叉树，以及目标和 `sum = 22`，
                          5                 / \                4   8               /   / \              11  13  4             /  \    / \            7    2  5   1    

返回:
            3    **解释：** 和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]

提示：

  * `节点总数 <= 10000`


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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def v2(node,targetSum):
            res,leaf,que,cnt=[[[node.val]]],[],[[node,1,[]]],0
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+[node.val]])
                que.append([node.right,h+1,path+[node.val]])  
                pa = path+[node.val]
                res[h].append(pa)
                cum=0
                for j in range(len(pa)-1,-1,-1):
                    cum += pa[j]
                    if cum==targetSum:cnt+=1
            return cnt
        return v2(root,sum) if root else 0        
```

[title]: https://leetcode-cn.com/problems/paths-with-sum-lcci
