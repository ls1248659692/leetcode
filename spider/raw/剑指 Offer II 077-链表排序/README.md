# [链表排序][title]

## Description

给定链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)
            **输入：** head = [4,2,1,3]    **输出：** [1,2,3,4]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)
            **输入：** head = [-1,5,3,4,0]    **输出：** [-1,0,3,4,5]    

**示例 3：**
            **输入：** head = []    **输出：** []    



**提示：**

  * 链表中节点的数目在范围 `[0, 5 * 104]` 内
  * `-105 <= Node.val <= 105`



**进阶：** 你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？



注意：本题与主站 148 题相同：<https://leetcode-cn.com/problems/sort-list/>


**Tags:** Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
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

[title]: https://leetcode-cn.com/problems/7WHec2
