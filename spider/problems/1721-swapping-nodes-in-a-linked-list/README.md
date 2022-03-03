# [Swapping Nodes in a Linked List][title]

## Description

给你链表的头节点 `head` 和一个整数 `k` 。

**交换** 链表正数第 `k` 个节点和倒数第 `k` 个节点的值后，返回链表的头节点（链表 **从 1 开始索引** ）。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2021/01/10/linked1.jpg)
            **输入：** head = [1,2,3,4,5], k = 2    **输出：** [1,4,3,2,5]    

**示例 2：**
            **输入：** head = [7,9,6,6,7,8,3,0,9,5], k = 5    **输出：** [7,9,6,6,8,7,3,0,9,5]    

**示例 3：**
            **输入：** head = [1], k = 1    **输出：** [1]    

**示例 4：**
            **输入：** head = [1,2], k = 1    **输出：** [2,1]    

**示例 5：**
            **输入：** head = [1,2,3], k = 2    **输出：** [1,2,3]    

**提示：**

  * 链表中节点的数目是 `n`
  * `1 <= k <= n <= 105`
  * `0 <= Node.val <= 100`


**Tags:** Linked List, Two Pointers

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list
