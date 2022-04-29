# [链表中的两数相加][title]

## Description

给定两个 **非空链表** `l1`和 `l2`
来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

可以假设除了数字 0 之外，这两个数字都不会以零开头。



**示例1：**

![](https://pic.leetcode-cn.com/1626420025-fZfzMX-image.png)
            **输入：** l1 = [7,2,4,3], l2 = [5,6,4]    **输出：** [7,8,0,7]    

**示例2：**
            **输入：** l1 = [2,4,3], l2 = [5,6,4]    **输出：** [8,0,7]    

**示例3：**
            **输入：** l1 = [0], l2 = [0]    **输出：** [0]    



**提示：**

  * 链表的长度范围为` [1, 100]`
  * `0 <= node.val <= 9`
  * 输入数据保证链表代表的数字无前导 0



**进阶：** 如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。



注意：本题与主站 445 题相同：<https://leetcode-cn.com/problems/add-two-numbers-ii/>


**Tags:** Stack, Linked List, Math

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

        # def lkl2ls(lkn):
        #     tli =[]
        #     while lkn: 
        #         tli.append(lkn.val)
        #         lkn= lkn.next
        #     return tli

        # def lkl2str(lkn):
        #     tli =[]
        #     while lkn or (tli.append(lkn.val) and lkn ):  lkn= lkn.next
        #     return ''.join([str(e) for e in tli])

        str1,str2 = '','' 
        while l1: l1,str1 = l1.next,str(l1.val) + str1
        while l2: l2,str2 = l2.next,str(l2.val) + str2
            
        result = str(int(str1[::-1]) + int(str2[::-1]))
        return lkl([int(i) for i in result])        
```

[title]: https://leetcode-cn.com/problems/lMSNwu
