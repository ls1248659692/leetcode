# [Rotate List][title]

## Description

给你一个链表的头节点 `head` ，旋转链表，将链表每个节点向右移动 `k` __ 个位置。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)
            **输入：** head = [1,2,3,4,5], k = 2    **输出：** [4,5,1,2,3]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)
            **输入：** head = [0,1,2], k = 4    **输出：** [2,0,1]    

**提示：**

  * 链表中节点的数目在范围 `[0, 500]` 内
  * `-100 <= Node.val <= 100`
  * `0 <= k <= 2 * 109`


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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return None
        tls = []
        while head:
            tls.append(head)
            head =head.next       
        
        k=k%len(tls)

        nt=tls[-k:]+tls[:-k]
        for i in range(len(nt)-1):
            nt[i].next=nt[i+1]
        nt[-1].next=None
        return nt[0]
```

[title]: https://leetcode-cn.com/problems/rotate-list
