# [Print Immutable Linked List in Reverse][title]

## Description

给您一个不可变的链表，使用下列接口逆序打印每个节点的值：

  * `ImmutableListNode`: 描述不可变链表的接口，链表的头节点已给出。

您需要使用以下函数来访问此链表（您  **不能  **直接访问 `ImmutableListNode`）：

  * `ImmutableListNode.printValue()`：打印当前节点的值。
  * `ImmutableListNode.getNext()`：返回下一个节点。

输入只用来内部初始化链表。您不可以通过修改链表解决问题。也就是说，您只能通过上述 API 来操作链表。



**示例 1：**
            **输入：** head = [1,2,3,4]    **输出：** [4,3,2,1]    

**示例 2：**
            **输入：** head = [0,-4,-1,3,-5]    **输出：** [-5,3,-1,-4,0]    

**示例 3：**
            **输入：** head = [-2,0,6,4,4,-6]    **输出：** [-6,4,4,6,0,-2]    



**提示：**

  * 链表的长度在 `[1, 1000]` 之间。
  * 每个节点的值在 `[-1000, 1000]` 之间。



**进阶：**

您是否可以：

  * 使用常数级空间复杂度解决问题？
  * 使用线性级时间复杂度和低于线性级空间复杂度解决问题？


**Tags:** Stack, Recursion, Linked List, Two Pointers

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/print-immutable-linked-list-in-reverse
