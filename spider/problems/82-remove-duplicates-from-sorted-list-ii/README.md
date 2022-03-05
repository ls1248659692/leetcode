# [Remove Duplicates from Sorted List II][title]

## Description

给定一个已排序的链表的头 `head` ，  _删除原始链表中所有重复数字的节点，只留下不同的数字_  。返回 _已排序的链表_  。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)
            **输入：** head = [1,2,3,3,4,4,5]    **输出：** [1,2,5]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)
            **输入：** head = [1,1,1,2,3]    **输出：** [2,3]    



**提示：**

  * 链表中节点数目在范围 `[0, 300]` 内
  * `-100 <= Node.val <= 100`
  * 题目数据保证链表已经按升序 **排列**


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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)
        if not lst:return None 
        d={}
        for e in lst:
            d[e.val]= d.get(e.val,0)+1
        single = [k for k,v in d.items() if v>=2]
        l2 = [e for e in lst if e.val not in single]
        if not l2:return None
        for i in range(len(l2)-1):
            l2[i].next=l2[i+1]
        l2[-1].next=None
        return l2[0]
```

[title]: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
