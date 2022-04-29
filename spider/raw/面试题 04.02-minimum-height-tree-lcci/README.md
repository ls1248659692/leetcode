# [Minimum Height Tree LCCI][title]

## Description

给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

 **示例:**
            给定有序数组: [-10,-3,0,5,9],            一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：                      0                / \              -3   9              /   /            -10  5       


**Tags:** Tree, Binary Search Tree, Array, Divide and Conquer, Binary Tree

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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        root = TreeNode(nums[len(nums)//2])
        root.left,root.right = self.sortedArrayToBST(nums[: len(nums)//2]), self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root        
```

[title]: https://leetcode-cn.com/problems/minimum-height-tree-lcci
