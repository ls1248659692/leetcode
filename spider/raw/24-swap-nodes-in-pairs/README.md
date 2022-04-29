# [Swap Nodes in Pairs][title]

## Description

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)
            **输入：** head = [1,2,3,4]    **输出：** [2,1,4,3]    

**示例 2：**
            **输入：** head = []    **输出：** []    

**示例 3：**
            **输入：** head = [1]    **输出：** [1]    



**提示：**

  * 链表中节点的数目在范围 `[0, 100]` 内
  * `0 <= Node.val <= 100`


**Tags:** Recursion, Linked List

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def lkl2ls(lkn):
    tli = []
    while lkn:
        tli.append(lkn)
        lkn = lkn.next
    return tli

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tli = lkl2ls(head)
        # if len(tli)<=1:return head
        mod = len(tli)%2
        for i in range(0,len(tli)-mod,2):
            tli[i+1].next, tli[i].next =tli[i], tli[i+3-(mod if mod and i+3-mod==len(tli)-1 else 0)] if i+3-mod < len(tli) else None
        return tli[1] if len(tli)>1 else head  
```

[title]: https://leetcode-cn.com/problems/swap-nodes-in-pairs
