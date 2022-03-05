# [Remove Duplicates from Sorted List][title]

## Description

给定一个已排序的链表的头 `head` ，  _删除所有重复的元素，使每个元素只出现一次_  。返回 _已排序的链表_  。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)
            **输入：** head = [1,1,2]    **输出：** [1,2]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/04/list2.jpg)
            **输入：** head = [1,1,2,3,3]    **输出：** [1,2,3]    



**提示：**

  * 链表中节点数目在范围 `[0, 300]` 内
  * `-100 <= Node.val <= 100`
  * 题目数据保证链表已经按升序 **排列**


**Tags:** Linked List

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = head
        if not t or not t.next: return t
        cli =[t]
        while t.next:
            t=t.next
            if cli and t.val ==cli[-1].val:
                cli[-1].next=t.next   
            else:         
                cli.append(t)
            
            
        if cli and t.val ==cli[-1].val: cli[-1].next=t.next
        return cli[0]
```

[title]: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
