# [Palindrome Linked List][title]

## Description

给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)
            **输入：** head = [1,2,2,1]    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)
            **输入：** head = [1,2]    **输出：** false    



**提示：**

  * 链表中节点数目在范围`[1, 105]` 内
  * `0 <= Node.val <= 9`



**进阶：** 你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？


**Tags:** Stack, Recursion, Linked List, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        t = head
        if not t or not t.next: return True
        cli =[t.val]
        while t.next:
            t=t.next
            cli.append(t.val)   
        #cli.append(t.val)
        print(cli)
        for i in range(len(cli)//2+1):
            if cli[i-1]!=cli[-i]:return False     
        return True
```

[title]: https://leetcode-cn.com/problems/palindrome-linked-list
