# [Kth Node From End of List LCCI][title]

## Description

实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

**注意：** 本题相对原题稍作改动

**示例：**
            **输入：** 1->2->3->4->5 和 _k_ = 2    **输出：** 4

**说明：**

给定的 _k_  保证是有效的。


**Tags:** Linked List, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)
        return lst[-k].val        
```

[title]: https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
