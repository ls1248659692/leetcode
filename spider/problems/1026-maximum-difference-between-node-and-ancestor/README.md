# [Maximum Difference Between Node and Ancestor][title]

## Description

给定二叉树的根节点 `root`，找出存在于 **不同** 节点 `A` 和 `B` 之间的最大值 `V`，其中 `V = |A.val -
B.val|`，且 `A` 是 `B` 的祖先。

（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg)
            **输入：** root = [8,3,10,1,6,null,14,null,null,4,7,13]    **输出：** 7    **解释：**    我们有大量的节点与其祖先的差值，其中一些如下：    |8 - 3| = 5    |3 - 7| = 4    |8 - 1| = 7    |10 - 13| = 3    在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg)
            **输入：** root = [1,null,2,null,0,3]    **输出：** 3    

**提示：**

  * 树中的节点数在 `2` 到 `5000` 之间。
  * `0 <= Node.val <= 105`


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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def v2(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pathb =path+[node.val]
                que.append([node.left,h+1,pathb])
                que.append([node.right,h+1,pathb])  
                res[h].append(pathb)
                if not node.right and not node.left:
                    leaf.append(pathb)
            print(leaf)
            return leaf
        r=v2(root)
        return max(max(p)-min(p) for p in r)
```

[title]: https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor
