# [从尾到头打印链表 LCOF][title]

## Description

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



**示例 1：**
            **输入：** head = [1,3,2]    **输出：** [2,3,1]



**限制：**

`0 <= 链表长度 <= 10000`


**Tags:** Stack, Recursion, Linked List, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:return []
        t = head
        cli =[]
        while t:
            cli.append(t.val)
            t=t.next
        cli=cli[::-1]      
        print(cli)
        return cli
```

[title]: https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
