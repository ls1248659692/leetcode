# [链表中倒数第k个节点 LCOF][title]

## Description

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 `6` 个节点，从头节点开始，它们的值依次是 `1、2、3、4、5、6`。这个链表的倒数第 `3` 个节点是值为 `4` 的节点。

**示例：**
            给定一个链表: **1->2->3->4->5** , 和 _k_ **= 2**.        返回链表 4 **->5**.


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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        t = head
        cli =[]
        while t.next:
            cli.append(t)
            t=t.next
        cli.append(t)
        return cli[-k] if len(cli)>=k else cli[-k]
```

[title]: https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
