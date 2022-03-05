# [Sort Linked List Already Sorted Using Absolute Values][title]

## Description

给你一个链表的头结点 `head` ，这个链表是根据结点的 **绝对值** 进行 **升序** 排序, 返回重新根据 **节点的值** 进行 **升序**
排序的链表。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/10/17/image-20211017201240-3.png)
            **输入:** head = [0,2,-5,5,10,-10]    **输出:** [-10,-5,0,2,5,10]    **解释:**    根据结点的值的绝对值排序的链表是 [0,2,-5,5,10,-10].    根据结点的值排序的链表是 [-10,-5,0,2,5,10].    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/10/17/image-20211017201318-4.png)
            **输入:** head = [0,1,2]    **输出:** [0,1,2]    **解释:**    这个链表已经是升序的了。

**示例 3：**
            **输入:** head = [1]    **输出:** [1]    **解释:**    这个链表已经是升序的了。



**提示:**

  * 链表节点数的范围是 `[1, 105]`.
  * `-5000 <= Node.val <= 5000`
  * `head` 是根据结点绝对值升序排列好的链表.



**进阶:**

  * 你可以在`O(n)`的时间复杂度之内解决这个问题吗?


**Tags:** Linked List, Two Pointers, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/sort-linked-list-already-sorted-using-absolute-values
