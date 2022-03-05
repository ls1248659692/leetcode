# [Convert Binary Number in a Linked List to Integer][title]

## Description

给你一个单链表的引用结点 `head`。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 **十进制值** 。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/12/15/graph-1.png)
            **输入：** head = [1,0,1]    **输出：** 5    **解释：** 二进制数 (101) 转化为十进制数 (5)    

**示例 2：**
            **输入：** head = [0]    **输出：** 0    

**示例 3：**
            **输入：** head = [1]    **输出：** 1    

**示例 4：**
            **输入：** head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]    **输出：** 18880    

**示例 5：**
            **输入：** head = [0,0]    **输出：** 0    



**提示：**

  * 链表不为空。
  * 链表的结点总数不超过 `30`。
  * 每个结点的值不是 `0` 就是 `1`。


**Tags:** Linked List, Math

**Difficulty:** Easy

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s =''
        while head.next:
            s+= str(head.val)
            head=head.next
        s+= str(head.val)
        return int(s, base=2)
```

[title]: https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer
