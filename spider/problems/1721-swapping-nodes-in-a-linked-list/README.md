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

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        i,j = k-1,len(tls)-k
        if i==j:return tls[0]
        if i>j:  i,j= j,i
        if len(tls)==1 or j>=len(tls):return tls[0]
        print(i,j)
        if i==0:
            if i+1!=j:
                tls[j].next=tls[i+1]
                tls[j-1].next=tls[i]
                tls[i].next=None
            else:
                tls[i].next=None
                tls[j].next=tls[i]
            return tls[j]
        else:
            if i+1!=j:
                tls[i].next,tls[j].next=tls[j+1],tls[i+1]
                tls[i-1].next,tls[j-1].next=tls[j],tls[i]                
            else:
                tls[i].next=tls[j+1]
                tls[j].next=tls[i]
                tls[i-1].next=tls[j]
            return tls[0]

        # if k<len(tls) and tls[-k-1]!=tls[j]:
        #     tls[j].next=None
        #     tls[j-1].next=None
        #     tls[-k].next=None
        #     tls[-k-1].next=None
        #     tls[j-1].next= tls[-k]
        #     tls[-k-1].next=tls[j]
        #     tls[j].next=tls[-k+1]
        #     tls[-k].next=tls[j+1]
        # else:
        #     print('23234')
        #     tls[j].next=None
        #     if j-1>=0:tls[j-1].next=None
        #     if j+1<len(tls):tls[j+1].next=None
        #     if j-1>=0: tls[j-1].next= tls[j+1]     
        #     if j+1<len(tls):tls[j+1].next=tls[j]     
        #     if j+2<len(tls):
        #         tls[j].next= tls[j+2] 
        #     else:
        #         return tls[j+1]
            
        return tls[0]
```

[title]: https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list
