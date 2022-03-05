# [N-ary Tree Level Order Traversal][title]

## Description

给定一个 N 叉树，返回其节点值的 _层序遍历_ 。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
            **输入：** root = [1,null,3,2,4,null,5,6]    **输出：** [[1],[3,2,4],[5,6]]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
            **输入：** root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]    **输出：** [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]    

**提示：**

  * 树的高度不会超过 `1000`
  * 树的节点总数在 `[0, 10^4]` 之间


**Tags:** Tree, Breadth-First Search

**Difficulty:** Medium

## 思路

``` python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def v1(node):
            res,que=[[node.val]],[[node,1]]
            while que:
                node,h =que.pop(0)
                while len(res)<=h:res.append([])
                for ch in node.children:
                    res[h].append(ch.val)
                    que.append([ch,h+1])
            return res[:-1]         
        return v1(root) if root else []
```

[title]: https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal
