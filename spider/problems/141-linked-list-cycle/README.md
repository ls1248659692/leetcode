# [Linked List Cycle][title]

## Description

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos`
来表示链表尾连接到链表中的位置（索引从 0 开始）。 **注意：`pos` 不作为参数进行传递 **。仅仅是为了标识链表的实际情况。

_如果链表中存在环_  ，则返回 `true` 。 否则，返回 `false` 。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/07/circularlinkedlist.png)
            **输入：** head = [3,2,0,-4], pos = 1    **输出：** true    **解释：** 链表中有一个环，其尾部连接到第二个节点。    

**示例  2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/07/circularlinkedlist_test2.png)
            **输入：** head = [1,2], pos = 0    **输出：** true    **解释：** 链表中有一个环，其尾部连接到第一个节点。    

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/07/circularlinkedlist_test3.png)
            **输入：** head = [1], pos = -1    **输出：** false    **解释：** 链表中没有环。    



**提示：**

  * 链表中节点的数目范围是 `[0, 104]`
  * `-105 <= Node.val <= 105`
  * `pos` 为 `-1` 或者链表中的一个 **有效索引** 。



**进阶：** 你能用 `O(1)`（即，常量）内存解决此问题吗？


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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:return False
        n_li =[]
        while head.next and len(n_li)<10**4+1:
            n_li.append(head.val)
            head = head.next
        print(len(n_li))
        return len(n_li)==10**4+1
```

[title]: https://leetcode-cn.com/problems/linked-list-cycle
