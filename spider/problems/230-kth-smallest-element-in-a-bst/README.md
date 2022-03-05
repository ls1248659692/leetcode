# [Kth Smallest Element in a BST][title]

## Description

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` **** 个最小元素（从 1 开始计数）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)
            **输入：** root = [3,1,4,null,2], k = 1    **输出：** 1    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)
            **输入：** root = [5,3,6,2,4,null,null,1], k = 3    **输出：** 3    

**提示：**

  * 树中的节点数为 `n` 。
  * `1 <= k <= n <= 104`
  * `0 <= Node.val <= 104`

**进阶：** 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def midt(node):
            if not node: 
                pass
                #tli.append(None)
            else:
                if node.left: midt(node.left)       
                tli.append(node.val)      
                if node.right: midt(node.right)  

        tli=[]   
        midt(root)
        print(tli)
        return tli[k-1] if root else []       
```

[title]: https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
