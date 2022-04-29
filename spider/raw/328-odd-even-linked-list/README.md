# [Odd Even Linked List][title]

## Description

给定单链表的头节点 `head` ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

**第一个** 节点的索引被认为是 **奇数** ， **第二个** 节点的索引为  **偶数** ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

你必须在 `O(1)` 的额外空间复杂度和 `O(n)` 的时间复杂度下解决这个问题。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)
            **输入:** head = [1,2,3,4,5]    **输出:**  [1,3,5,2,4]

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)
            **输入:** head = [2,1,3,5,6,4,7]    **输出:** [2,3,6,7,1,5,4]



**提示:**

  * `n == ` 链表中的节点数
  * `0 <= n <= 104`
  * `-106 <= Node.val <= 106`


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
    def oddEvenList(self, head: ListNode) -> ListNode:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        tls = [e for i,e in enumerate(tls) if i%2==0] + [e for i,e in enumerate(tls) if i%2==1]
        if not tls :return None
        tls[-1].next=None
        for i in range(len(tls)-1):
            tls[i].next=tls[i+1]
        return tls[0]        
```

[title]: https://leetcode-cn.com/problems/odd-even-linked-list
