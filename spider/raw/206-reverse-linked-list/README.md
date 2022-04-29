# [Reverse Linked List][title]

## Description

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)
            **输入：** head = [1,2,3,4,5]    **输出：** [5,4,3,2,1]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)
            **输入：** head = [1,2]    **输出：** [2,1]    

**示例 3：**
            **输入：** head = []    **输出：** []    

**提示：**

  * 链表中节点的数目范围是 `[0, 5000]`
  * `-5000 <= Node.val <= 5000`

**进阶：** 链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？


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
    def reverseList(self, head: ListNode) -> ListNode:
        h_li=[]
        tmp_h = head
        if not tmp_h: return None
        while tmp_h.next:
            h_li.append(tmp_h.val)
            tmp_h =tmp_h.next
        h_li.append(tmp_h.val)
        h_li.reverse()
        # print(h_li)
        r_ln = ListNode(h_li[-1])
        for ii in range(len(h_li)-2,-1,-1):
            r_ln = ListNode(h_li[ii],r_ln)
        # print(r_ln)
        return r_ln

```

[title]: https://leetcode-cn.com/problems/reverse-linked-list
