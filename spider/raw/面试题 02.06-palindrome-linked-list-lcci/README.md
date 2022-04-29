# [Palindrome Linked List LCCI][title]

## Description

编写一个函数，检查输入的链表是否是回文的。



**示例 1：**
            **输入：** 1->2    **输出：** false     

**示例 2：**
            **输入：** 1->2->2->1    **输出：** true     



**进阶：**  
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


**Tags:** Stack, Recursion, Linked List, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)      
        lst = [e.val for e in lst]
        for i in range(1,len(lst)//2+1):
            if lst[i-1]!=lst[-i]:return False
        return True 
```

[title]: https://leetcode-cn.com/problems/palindrome-linked-list-lcci
