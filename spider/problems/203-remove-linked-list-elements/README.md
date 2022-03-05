# [Remove Linked List Elements][title]

## Description

给你一个链表的头节点 `head` 和一个整数 `val` ，请你删除链表中所有满足 `Node.val == val` 的节点，并返回 **新的头节点**
。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)
            **输入：** head = [1,2,6,3,4,5,6], val = 6    **输出：** [1,2,3,4,5]    

**示例 2：**
            **输入：** head = [], val = 1    **输出：** []    

**示例 3：**
            **输入：** head = [7,7,7,7], val = 7    **输出：** []    

**提示：**

  * 列表中的节点数目在范围 `[0, 104]` 内
  * `1 <= Node.val <= 50`
  * `0 <= val <= 50`


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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def c2li(head):
            li =[]
            while head.next:
                li.append(head)
                head=head.next
            li.append(head)
            return li
        if not head:return None
        cli = c2li(head)
        for i in range(len(cli)-1,0,-1):
            if cli[i].val == val:
                cli[i-1].next = cli[i].next
        tcli = [l for l in cli if l.val!=val]
        return tcli[0] if tcli else None
```

[title]: https://leetcode-cn.com/problems/remove-linked-list-elements
