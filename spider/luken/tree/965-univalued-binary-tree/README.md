# [Univalued Binary Tree][title]

## Description

如果二叉树每个节点都具有相同的值，那么该二叉树就是 _单值_ 二叉树。

只有给定的树是单值二叉树时，才返回 `true`；否则返回 `false`。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-
shot-2018-12-25-at-50104-pm.png)
            **输入：** [1,1,1,1,1,null,1]    **输出：** true    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-
shot-2018-12-25-at-50050-pm.png)
            **输入：** [2,2,2,5,2]    **输出：** false    



**提示：**

  1. 给定树的节点数范围是 `[1, 100]`。
  2. 每个节点的值都是整数，范围为 `[0, 99]` 。


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
    def isUnivalTree(self, root: TreeNode) -> bool:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order]+[dd*unit]]
            else:
                res= [[nd.val,order]+[dd]] + trs(nd.left,'r%d'%nd.val,nullv,dd+1) + trs(nd.right,'r%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r%d'%root.val,[None],1) 
        nli = [el[0] for el in tli if el[0] is not None]
        print(tli)        
        return len(set(nli))==1
```

[title]: https://leetcode-cn.com/problems/univalued-binary-tree
