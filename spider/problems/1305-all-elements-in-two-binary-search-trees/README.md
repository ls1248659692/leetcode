# [All Elements in Two Binary Search Trees][title]

## Description

给你 `root1` 和 `root2` 这两棵二叉搜索树。请你返回一个列表，其中包含  **两棵树  **中的所有整数并按 **升序** 排序。.



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/12/29/q2-e1.png)
            **输入：** root1 = [2,1,4], root2 = [1,0,3]    **输出：** [0,1,1,2,3,4]    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/12/29/q2-e5-.png)
            **输入：** root1 = [1,null,8], root2 = [8,1]    **输出：** [1,1,8,8]    



**提示：**

  * 每棵树的节点数在 `[0, 5000]` 范围内
  * `-105 <= Node.val <= 105`


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree, Sorting

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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def v1(node): 
            tli,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tli.append(node.val)
                node = node.right 
            return tli

        return sorted(v1(root1)+v1(root2))           
```

[title]: https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees
