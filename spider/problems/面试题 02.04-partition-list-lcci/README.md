# [Partition List LCCI][title]

## Description

给你一个链表的头节点 `head` 和一个特定值 __`x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于**
`x` 的节点之前。

你不需要  **保留**  每个分区中各节点的初始相对位置。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)
            **输入：** head = [1,4,3,2,5,2], x = 3    **输出** ：[1,2,2,4,3,5]    

**示例 2：**
            **输入：** head = [2,1], x = 2    **输出** ：[1,2]    



**提示：**

  * 链表中节点的数目在范围 `[0, 200]` 内
  * `-100 <= Node.val <= 100`
  * `-200 <= x <= 200`


**Tags:** Linked List, Two Pointers

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        def lkl2ls(lkn):
            tli =[]
            while lkn:
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)   
        tls = [e for e in tls if e.val < x] +[e for e in tls if e.val >= x]    
        if not tls :return None
        tls[-1].next=None
        for i in range(len(tls)-1):
            tls[i].next=tls[i+1]
        return tls[0]        
```

[title]: https://leetcode-cn.com/problems/partition-list-lcci
