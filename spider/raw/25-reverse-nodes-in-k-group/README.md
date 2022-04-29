# [Reverse Nodes in k-Group][title]

## Description

给你一个链表，每 _k_ 个节点一组进行翻转，请你返回翻转后的链表。

_k_ 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 _k_ 的整数倍，那么请将最后剩余的节点保持原有顺序。

**进阶：**

  * 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
  * **你不能只是单纯的改变节点内部的值** ，而是需要实际进行节点交换。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)
            **输入：** head = [1,2,3,4,5], k = 2    **输出：** [2,1,4,3,5]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)
            **输入：** head = [1,2,3,4,5], k = 3    **输出：** [3,2,1,4,5]    

**示例 3：**
            **输入：** head = [1,2,3,4,5], k = 1    **输出：** [1,2,3,4,5]    

**示例 4：**
            **输入：** head = [1], k = 1    **输出：** [1]    

**提示：**

  * 列表中节点的数量在范围 `sz` 内
  * `1 <= sz <= 5000`
  * `0 <= Node.val <= 1000`
  * `1 <= k <= sz`


**Tags:** Recursion, Linked List

**Difficulty:** Hard

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def toli(head):
            tli =[]
            while head.next:
                tli.append(head)
                head = head.next
            tli.append(head)
            return tli

        if not head:return None
        tli = toli(head)      
        if len(tli)==1:return head
        if k==1: return head

        md = len(tli)% k
        for i in range(0,len(tli)-md,k):
            if md!=0 and i+k>= len(tli)-md-1:
                 tli[i].next =tli[i+k]
            else:
                tli[i].next =tli[i+2*k-1] if i+2*k-1 < len(tli) else None
            for t in range(1,k):
               tli[i+t].next = tli[i+t-1]

        return  tli[k-1]        
```

[title]: https://leetcode-cn.com/problems/reverse-nodes-in-k-group
