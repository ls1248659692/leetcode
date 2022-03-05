# [Insertion Sort List][title]

## Description

给定单个链表的头 `head` ，使用 **插入排序** 对链表进行排序，并返回  _排序后链表的头_  。

**插入排序**  算法的步骤:

  1. 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
  2. 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
  3. 重复直到所有输入数据插入完为止。

下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。

对链表进行插入排序。

![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-
example-300px.gif)



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg)
            **输入:** head = [4,2,1,3]    **输出:** [1,2,3,4]

**示例  2：**

![](https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg)
            **输入:** head = [-1,5,3,4,0]    **输出:** [-1,0,3,4,5]



**提示：**

  * 列表中的节点数在 `[1, 5000]`范围内
  * `-5000 <= Node.val <= 5000`


**Tags:** Linked List, Sorting

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        tls = sorted(tls,key=lambda xx:xx.val)
        if not tls :return None
        tls[-1].next=None
        for i in range(len(tls)-1):
            tls[i].next=tls[i+1]
        return tls[0]        
```

[title]: https://leetcode-cn.com/problems/insertion-sort-list
