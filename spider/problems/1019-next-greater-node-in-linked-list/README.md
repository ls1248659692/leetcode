# [Next Greater Node In Linked List][title]

## Description

给定一个长度为 `n` 的链表 `head`

对于列表中的每个节点，查找下一个 **更大节点** 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 **严格大于** 它的值。

返回一个整数数组 `answer` ，其中 `answer[i]` 是第 `i` 个节点( **从1开始** )的下一个更大的节点的值。如果第 `i`
个节点没有下一个更大的节点，设置 `answer[i] = 0` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg)
            **输入：** head = [2,1,5]    **输出：** [5,5,0]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext2.jpg)
            **输入：** head = [2,7,4,3,5]    **输出：** [7,0,5,5,0]    



**提示：**

  * 链表中节点数为 `n`
  * `1 <= n <= 104`
  * `1 <= Node.val <= 109`


**Tags:** Stack, Array, Linked List, Monotonic Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/next-greater-node-in-linked-list
