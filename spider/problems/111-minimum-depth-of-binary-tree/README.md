# [Minimum Depth of Binary Tree][title]

## Description

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明：** 叶子节点是指没有子节点的节点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)
            **输入：** root = [3,9,20,null,null,15,7]    **输出：** 2    

**示例 2：**
            **输入：** root = [2,null,3,null,4,null,5,null,6]    **输出：** 5    

**提示：**

  * 树中节点数的范围在 `[0, 105]` 内
  * `-1000 <= Node.val <= 1000`


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
    def minDepth(self, root: TreeNode) -> int:
        unit = 100000
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val]+[dd*unit]]
            else:
                if order=='pre':
                    res= [[nd.val]+[dd]] + trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1)
                if order=='pos':
                    res = trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1) +[[nd.val]+[dd]]
            return res        
        tli = trs(root,'pre',[None],1)
        #print(tli)
        return min(el[1]//unit for el in tli if el[1]>=unit) if root else 0
```

[title]: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
