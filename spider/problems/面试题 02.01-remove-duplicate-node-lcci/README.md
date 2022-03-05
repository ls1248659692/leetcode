# [Remove Duplicate Node LCCI][title]

## Description

编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

**示例1:**
            **输入** ：[1, 2, 3, 3, 2, 1]    **输出** ：[1, 2, 3]    

**示例2:**
            **输入** ：[1, 1, 1, 1, 2]    **输出** ：[1, 2]    

**提示：**

  1. 链表长度在[0, 20000]范围内。
  2. 链表元素在[0, 20000]范围内。

**进阶：**

如果不得使用临时缓冲区，该怎么解决？


**Tags:** Hash Table, Linked List, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)
        if not lst:return None 
        d,l2={},[]
        for e in lst:
            if e.val not in d:
                l2.append(e)
            d[e.val]= d.get(e.val,0)+1
        if not l2:return None
        for i in range(len(l2)-1):
            l2[i].next=l2[i+1]
        l2[-1].next=None
        return l2[0]        
```

[title]: https://leetcode-cn.com/problems/remove-duplicate-node-lcci
