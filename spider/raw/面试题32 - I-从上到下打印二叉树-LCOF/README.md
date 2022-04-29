# [从上到下打印二叉树 LCOF][title]

## Description

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。



例如:  
给定二叉树: `[3,9,20,null,null,15,7]`,
                3       / \      9  20        /  \       15   7    

返回：
            [3,9,20,15,7]    



**提示：**

  1. `节点总数 <= 1000`


**Tags:** Tree, Breadth-First Search, Binary Tree

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
    def levelOrder(self, root: TreeNode) -> List[int]:
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
            return res[:-1] if len(res)>=2 else res    
        return [e for r in v1(root) for e in r]  if root else []       
```

[title]: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
