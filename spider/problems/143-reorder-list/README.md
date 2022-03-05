# [Reorder List][title]

## Description

给定一个单链表 `L` __ 的头节点 `head` ，单链表 `L` 表示为：
            L0 → L1 → … → Ln - 1 → Ln    

请将其重新排列后变为：
            L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



**示例 1：**

![](https://pic.leetcode-cn.com/1626420311-PkUiGI-image.png)
            **输入：** head = [1,2,3,4]    **输出：** [1,4,2,3]

**示例 2：**

![](https://pic.leetcode-cn.com/1626420320-YUiulT-image.png)
            **输入：** head = [1,2,3,4,5]    **输出：** [1,5,2,4,3]



**提示：**

  * 链表的长度范围为 `[1, 5 * 104]`
  * `1 <= node.val <= 1000`


**Tags:** Stack, Recursion, Linked List, Two Pointers

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        if not tls :return None
        for i in range(len(tls)): tls[i].next=None

        nt = []
        n= len(tls)-1
            
        for i in range((len(tls)+1)//2):
            nt.append(tls[i])
            if n-i!=i: nt.append(tls[n-i])

        tls = nt
        
        tls[-1].next=None
        for i in range(len(tls)-1):
            tls[i].next=tls[i+1]
        head= tls[0]
        return head        
```

[title]: https://leetcode-cn.com/problems/reorder-list
