# [Cousins in Binary Tree][title]

## Description

在二叉树中，根节点位于深度 `0` 处，每个深度为 `k` 的节点的子节点位于深度 `k+1` 处。

如果二叉树的两个节点深度相同，但 **父节点不同** ，则它们是一对 _堂兄弟节点_ 。

我们给出了具有唯一值的二叉树的根节点 `root` ，以及树中两个不同节点的值 `x` 和 `y` 。

只有与值 `x` 和 `y` 对应的节点是堂兄弟节点时，才返回 `true` 。否则，返回 `false`。

**示例 1：  
![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/16/q1248-01.png)**
            **输入：** root = [1,2,3,4], x = 4, y = 3    **输出：** false    

**示例 2：  
![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/16/q1248-02.png)**
            **输入：** root = [1,2,3,null,4,null,5], x = 5, y = 4    **输出：** true    

**示例 3：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/16/q1248-03.png)**
            **输入：** root = [1,2,3,null,4], x = 2, y = 3    **输出：** false

**提示：**

  * 二叉树的节点数介于 `2` 到 `100` 之间。
  * 每个节点的值都是唯一的、范围为 `1` 到 `100` 的整数。


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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order]+[dd*unit]]
            else:
                res= [[nd.val,order]+[dd]] + trs(nd.left,'r%d'%nd.val,nullv,dd+1) + trs(nd.right,'r%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r%d'%root.val,[None],1) 
        print(tli)
        xyli = [el for el in tli if el[0] in(x,y)]      
        return xyli[0][-1]== xyli[1][-1] and xyli[0][-2]!= xyli[1][-2]
```

[title]: https://leetcode-cn.com/problems/cousins-in-binary-tree
