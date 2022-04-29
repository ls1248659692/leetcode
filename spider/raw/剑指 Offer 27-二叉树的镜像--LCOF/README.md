# [二叉树的镜像  LCOF][title]

## Description

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

`     4  
   /   \  
  2     7  
 / \   / \  
1   3 6   9`  
镜像输出：

`     4  
   /   \  
  7     2  
 / \   / \  
9   6 3   1`



**示例 1：**
            **输入：** root = [4,2,7,1,3,6,9]    **输出：** [4,7,2,9,6,3,1]    



**限制：**

`0 <= 节点个数 <= 1000`

注意：本题与主站 226 题相同：<https://leetcode-cn.com/problems/invert-binary-tree/>


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
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def trs_v4(nd):
            if not nd:return nd
            elif  not nd.left and not nd.right:return nd
            else:
                n_left = trs_v4(nd.left) if nd.left else None
                n_rigt = trs_v4(nd.right)  if nd.right else None
                if nd.left or nd.right:
                    nd.right,nd.left= n_left,n_rigt
                return nd

        return trs_v4(root)        
```

[title]: https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
