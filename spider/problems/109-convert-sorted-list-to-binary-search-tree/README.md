# [Convert Sorted List to Binary Search Tree][title]

## Description

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树 _每个节点  _的左右两个子树的高度差的绝对值不超过 1。

**示例:**
            给定的有序链表： [-10, -3, 0, 5, 9],        一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：              0         / \       -3   9       /   /     -10  5    


**Tags:** Tree, Binary Search Tree, Linked List, Divide and Conquer, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def ld2lis(head):
            r=[]
            if not head: return r
            while head.next:
                r.append(head)
                head=head.next
            r.append(head)
            return r

        def ar2bst(nums):     
            if not nums: return None
            root_index = len(nums)//2
            root = TreeNode(nums[root_index])
            root.left = ar2bst(nums[:root_index])
            root.right = ar2bst(nums[root_index+1:])
            return root       

        ls =ld2lis(head)
        vls = [e.val for e in ls]
        return ar2bst(vls)
```

[title]: https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
