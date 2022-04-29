# [Merge Two Sorted Lists][title]

## Description

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)
            **输入：** l1 = [1,2,4], l2 = [1,3,4]    **输出：** [1,1,2,3,4,4]    

**示例 2：**
            **输入：** l1 = [], l2 = []    **输出：** []    

**示例 3：**
            **输入：** l1 = [], l2 = [0]    **输出：** [0]    

**提示：**

  * 两个链表的节点数目范围是 `[0, 50]`
  * `-100 <= Node.val <= 100`
  * `l1` 和 `l2` 均按 **非递减顺序** 排列


**Tags:** Recursion, Linked List

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

[title]: https://leetcode-cn.com/problems/merge-two-sorted-lists
