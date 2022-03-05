# [Add Two Numbers][title]

## Description

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2021/01/02/addtwonumber1.jpg)
            **输入：** l1 = [2,4,3], l2 = [5,6,4]    **输出：** [7,0,8]    **解释：** 342 + 465 = 807.    

**示例 2：**
            **输入：** l1 = [0], l2 = [0]    **输出：** [0]    

**示例 3：**
            **输入：** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]    **输出：** [8,9,9,9,0,0,0,1]    

**提示：**

  * 每个链表中的节点数在范围 `[1, 100]` 内
  * `0 <= Node.val <= 9`
  * 题目数据保证列表表示的数字不含前导零


**Tags:** Recursion, Linked List, Math

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def lkl(ls):
            lkn = ListNode(ls[0])
            head =lkn
            for n in ls[1:]:
                lkn.next=ListNode(n)
                lkn=lkn.next
            return head

        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn.val)
                lkn= lkn.next
            return tli

        def lkl2str(lkn):
            tli =[]
            while lkn or (tli.append(lkn.val) and lkn ):  lkn= lkn.next
            return ''.join([str(e) for e in tli])

        str1,str2 = '','' 
        while l1: l1,str1 = l1.next,str(l1.val) + str1
        while l2: l2,str2 = l2.next,str(l2.val) + str2
            
        result = str(int(str1) + int(str2))[::-1]
        return lkl([int(i) for i in result])
```

[title]: https://leetcode-cn.com/problems/add-two-numbers
