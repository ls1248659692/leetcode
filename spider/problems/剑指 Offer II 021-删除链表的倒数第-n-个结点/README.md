# [删除链表的倒数第 n 个结点][title]

## Description

给定一个链表，删除链表的倒数第 `n` _ _ 个结点，并且返回链表的头结点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
            **输入：** head = [1,2,3,4,5], n = 2    **输出：** [1,2,3,5]    

**示例 2：**
            **输入：** head = [1], n = 1    **输出：** []    

**示例 3：**
            **输入：** head = [1,2], n = 1    **输出：** [1]    



**提示：**

  * 链表中结点的数目为 `sz`
  * `1 <= sz <= 30`
  * `0 <= Node.val <= 100`
  * `1 <= n <= sz`



**进阶：** 能尝试使用一趟扫描实现吗？



注意：本题与主站 19 题相同： <https://leetcode-cn.com/problems/remove-nth-node-from-end-
of-list/>


**Tags:** Linked List, Two Pointers

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==1 and not head.next:return None
        tli =[]
        while head.next:
            tli.append(head)
            head = head.next
        tli.append(head)
        print(len(tli))
        if n>len(tli):return None
        if n==len(tli):return tli[1]
        tli[-n-1].next = tli[-n+1] if n>1 else None
        return tli[0]        
```

[title]: https://leetcode-cn.com/problems/SLwz0R
