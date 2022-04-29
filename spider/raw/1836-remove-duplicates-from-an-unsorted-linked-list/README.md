# [Remove Duplicates From an Unsorted Linked List][title]

## Description

给定一个链表的第一个节点 `head` ，找到链表中所有出现 **多于一次** 的元素，并删除这些元素所在的节点。

返回删除后的链表。

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/04/21/tmp-linked-list.jpg)
            **输入:** head = [1,2,3,2]    **输出:** [1,3]    **解释:** 2 在链表中出现了两次，所以所有的 2 都需要被删除。删除了所有的 2 之后，我们还剩下 [1,3] 。    

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/04/21/tmp-linked-list-1.jpg)
            **输入:** head = [2,1,1,2]    **输出:** []    **解释:** 2 和 1 都出现了两次。所有元素都需要被删除。    

**示例 3:**

![](https://assets.leetcode.com/uploads/2021/04/21/tmp-linked-list-2.jpg)
            **输入:** head = [3,2,2,1,3,2,4]    **输出:** [1,4]    **解释:** 3 出现了两次，且 2 出现了三次。移除了所有的 3 和 2 后，我们还剩下 [1,4] 。    

**提示：**

  * 链表中节点个数的范围是 `[1, 105]`
  * `1 <= Node.val <= 105`


**Tags:** Hash Table, Linked List

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/remove-duplicates-from-an-unsorted-linked-list
