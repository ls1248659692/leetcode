# [回文链表][title]

## Description

给定一个链表的 **头节点  **`head` **  ，**请判断其是否为回文链表。

如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。



**示例 1：**

**![](https://pic.leetcode-cn.com/1626421737-LjXceN-image.png)**
            **输入:** head = [1,2,3,3,2,1]    **输出:** true

**示例 2：**

**![](https://pic.leetcode-cn.com/1626422231-wgvnWh-image.png)**
            **输入:** head = [1,2]    **输出:** false    



**提示：**

  * 链表 L 的长度范围为 `[1, 105]`
  * `0 <= node.val <= 9`



**进阶：** 能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？



注意：本题与主站 234 题相同：<https://leetcode-cn.com/problems/palindrome-linked-list/>


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

[title]: https://leetcode-cn.com/problems/aMhZSa
