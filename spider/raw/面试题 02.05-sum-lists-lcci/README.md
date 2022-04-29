# [Sum Lists LCCI][title]

## Description

给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。



**示例：**
            **输入：** (7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295    **输出：** 2 -> 1 -> 9，即912    

**进阶：** 思考一下，假设这些数位是正向存放的，又该如何解决呢?

**示例：**
            **输入：** (6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295    **输出：** 9 -> 1 -> 2，即912    


**Tags:** Recursion, Linked List, Math

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def lkl(ls):
            lkn = ListNode(ls[0])
            head =lkn
            for n in ls[1:]:
                lkn.next=ListNode(n)
                lkn=lkn.next
            return head
            
        str1,str2 = '','' 
        while l1: l1,str1 = l1.next,str(l1.val) + str1
        while l2: l2,str2 = l2.next,str(l2.val) + str2
        print(str1,str2)
        result = str(int(str1) + int(str2)) #
        print(result)
        return lkl([int(i) for i in result[::-1]])          
```

[title]: https://leetcode-cn.com/problems/sum-lists-lcci
