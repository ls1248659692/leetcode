# [Reverse Linked List II][title]

## Description

给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left`
到位置 `right` 的链表节点，返回 **反转后的链表** 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)
            **输入：** head = [1,2,3,4,5], left = 2, right = 4    **输出：** [1,4,3,2,5]    

**示例 2：**
            **输入：** head = [5], left = 1, right = 1    **输出：** [5]    

**提示：**

  * 链表中节点数目为 `n`
  * `1 <= n <= 500`
  * `-500 <= Node.val <= 500`
  * `1 <= left <= right <= n`

**进阶：** 你可以使用一趟扫描完成反转吗？


**Tags:** Linked List

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        tls = []
        left,right=left-1,right-1
        while head:
            tls.append(head)
            head =head.next
        tls[left].next= None
        for i in range(left+1,right+1):
            print('chg',tls[i].val,tls[i-1].val)
            tls[i].next=tls[i-1]
        if right+1 <len(tls):tls[left].next=tls[right+1]
        print(left,right)
        if left-1>=0: tls[left-1].next=tls[right]
        return tls[0] if left-1>=0 else tls[right]
```

[title]: https://leetcode-cn.com/problems/reverse-linked-list-ii
