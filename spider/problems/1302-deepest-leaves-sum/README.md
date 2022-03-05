# [Deepest Leaves Sum][title]

## Description

给你一棵二叉树的根节点 `root` ，请你返回 **层数最深的叶子节点的和** 。

**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/12/28/1483_ex1.png)**
            **输入：** root = [1,2,3,4,5,null,6,7,null,null,null,null,8]    **输出：** 15    

**示例 2：**
            **输入：** root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]    **输出：** 19    

**提示：**

  * 树中节点数目在范围 `[1, 104]` 之间。
  * `1 <= Node.val <= 100`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def v1(node):
            res,que=[[node.val]],[[node,0]]
            while que:
                node,h =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(node.left.val)
                    que.append([node.left,h+1])
                if node.right:
                    res[h].append(node.right.val)
                    que.append([node.right,h+1])  
            return res[:-1]    
        res =v1(root)
        print(res)
        return sum(res[-1])
```

[title]: https://leetcode-cn.com/problems/deepest-leaves-sum
