# [链表中环的入口节点][title]

## Description

给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 `next` 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回
`null`。

为了表示给定链表中的环，我们使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 `pos` 是 `-1`，则在该链表中没有环。
**注意，`pos` 仅仅是用于标识环的情况，并不会作为参数传递到函数中。**

**说明：** 不允许修改给定的链表。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/07/circularlinkedlist.png)
            **输入：** head = [3,2,0,-4], pos = 1    **输出：** 返回索引为 1 的链表节点    **解释：** 链表中有一个环，其尾部连接到第二个节点。    

**示例  2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/07/circularlinkedlist_test2.png)
            **输入：** head = [1,2], pos = 0    **输出：** 返回索引为 0 的链表节点    **解释：** 链表中有一个环，其尾部连接到第一个节点。    

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/07/circularlinkedlist_test3.png)
            **输入：** head = [1], pos = -1    **输出：** 返回 null    **解释：** 链表中没有环。    



**提示：**

  * 链表中节点的数目范围在范围 `[0, 104]` 内
  * `-105 <= Node.val <= 105`
  * `pos` 的值为 `-1` 或者链表中的一个有效索引



**进阶：** 是否可以使用 `O(1)` 空间解决此题？



注意：本题与主站 142 题相同： <https://leetcode-cn.com/problems/linked-list-cycle-ii/>


**Tags:** Hash Table, Linked List, Two Pointers

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def lkl2ls(lkn):
            tli =[]
            while lkn and lkn not in tli: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        print([e.val for e in tls])
        if not tls or tls[-1].next is None:return None
        for i in range(len(tls)):
            if tls[i]==tls[-1].next:
                return tls[i]        
```

[title]: https://leetcode-cn.com/problems/c32eOV
