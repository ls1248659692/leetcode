# [Find Largest Value in Each Tree Row][title]

## Description

给定一棵二叉树的根节点 `root` ，请找出该二叉树中每一层的最大值。



**示例1：**

![](https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg)
            **输入:** root = [1,3,2,5,3,null,9]    **输出:** [1,3,9]    

**示例2：**
            **输入:** root = [1,2,3]    **输出:** [1,3]    



**提示：**

  * 二叉树的节点个数的范围是 `[0,104]`
  * `-231 <= Node.val <= 231 - 1`




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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def v1(node):
            res,que=[[node.val]],[[node,1]]
            while que:
                node,h =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(node.left.val)
                    que.append([node.left,h+1])
                if node.right:
                    res[h].append(node.right.val)
                    que.append([node.right,h+1])  
            print(res[:-1])
            return res[:-1]  

        return [max(r) for r in v1(root)] if root else []          
```

[title]: https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
