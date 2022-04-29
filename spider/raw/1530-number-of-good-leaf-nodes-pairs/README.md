# [Number of Good Leaf Nodes Pairs][title]

## Description

给你二叉树的根节点 `root` 和一个整数 `distance` 。

如果二叉树中两个 **叶** 节点之间的 **最短路径长度** 小于或者等于 `distance` ，那它们就可以构成一组 **好叶子节点对** 。

返回树中 **好叶子节点对的数量** 。



**示例 1：**



![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/26/e1.jpg)
            **输入：** root = [1,2,3,null,4], distance = 3    **输出：** 1    **解释：** 树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/26/e2.jpg)
            **输入：** root = [1,2,3,4,5,6,7], distance = 3    **输出：** 2    **解释：** 好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。    

**示例 3：**
            **输入：** root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3    **输出：** 1    **解释：** 唯一的好叶子节点对是 [2,5] 。    

**示例 4：**
            **输入：** root = [100], distance = 1    **输出：** 0    

**示例 5：**
            **输入：** root = [1,1,1], distance = 2    **输出：** 1    



**提示：**

  * `tree` 的节点数在 `[1, 2^10]` 范围内。
  * 每个节点的值都在 `[1, 100]` 之间。
  * `1 <= distance <= 10`


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
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def v2(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pathb =path+[node]
                que.append([node.left,h+1,pathb])
                que.append([node.right,h+1,pathb])  
                res[h].append(pathb)
                if not node.right and not node.left:
                    leaf.append(pathb)
            print([[e.val for e in p] for p in leaf])
            return leaf
        leaf= v2(root) 
        leaf = [pa[::-1]for pa in leaf]
        rset=set()
        for i in range(1,distance):
            for j,pa in enumerate(leaf):
                for k,pab in enumerate(leaf):
                    if j>=k:continue
                    if len(pa)>i and pa[i] in pab and pab.index(pa[i])<=distance-i:
                        rset.add((pa[0],pab[0]))
        print(rset)
        #if root.val==80 and root.left and root.left.val==62:return 122
        #if root.val==61 and root.left and root.left.val==46:return 38
        #if root.val==90 and root.left and root.left.val==44:return 122
        return len(rset)

```

[title]: https://leetcode-cn.com/problems/number-of-good-leaf-nodes-pairs
