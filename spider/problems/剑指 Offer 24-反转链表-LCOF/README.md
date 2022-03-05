# [反转链表 LCOF][title]

## Description

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。



**示例:**
            **输入:** 1->2->3->4->5->NULL    **输出:** 5->4->3->2->1->NULL



**限制：**

`0 <= 节点个数 <= 5000`



**注意** ：本题与主站 206 题相同：<https://leetcode-cn.com/problems/reverse-linked-list/>


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
    def reverseList(self, head: ListNode) -> ListNode:
        h_li=[]
        tmp_h = head
        if not tmp_h: return None
        while tmp_h:
            h_li.append(tmp_h.val)
            tmp_h =tmp_h.next
        h_li.reverse()
        # print(h_li)
        r_ln = ListNode(h_li[-1])
        for ii in range(len(h_li)-2,-1,-1):
            r_ln = ListNode(h_li[ii],r_ln)
        # print(r_ln)
        return r_ln
```

[title]: https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
