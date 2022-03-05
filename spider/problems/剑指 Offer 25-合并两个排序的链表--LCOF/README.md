# [合并两个排序的链表  LCOF][title]

## Description

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

**示例1：**
            **输入：** 1->2->4, 1->3->4    **输出：** 1->1->2->3->4->4

**限制：**

`0 <= 链表长度 <= 1000`

注意：本题与主站 21 题相同：<https://leetcode-cn.com/problems/merge-two-sorted-lists/>


**Tags:** Recursion, Linked List

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1,list2=l1,l2
        li_1=[]
        if list1:
            while list1.next:
                li_1.append(list1.val)
                list1=list1.next
            li_1.append(list1.val)
        if list2:
            while list2.next:
                li_1.append(list2.val)
                list2=list2.next
            li_1.append(list2.val)     

        li_1.sort()
        li_1.reverse() 
        if not li_1:return None
        res = ListNode(li_1[0])
        for el in li_1[1:]:
            res=ListNode(el,next=res)
        return res

```

[title]: https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
