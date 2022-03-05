# [Merge k Sorted Lists][title]

## Description

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



**示例 1：**
            **输入：** lists = [[1,4,5],[1,3,4],[2,6]]    **输出：** [1,1,2,3,4,4,5,6]    **解释：** 链表数组如下：    [      1->4->5,      1->3->4,      2->6    ]    将它们合并到一个有序链表中得到。    1->1->2->3->4->4->5->6    

**示例 2：**
            **输入：** lists = []    **输出：** []    

**示例 3：**
            **输入：** lists = [[]]    **输出：** []    



**提示：**

  * `k == lists.length`
  * `0 <= k <= 10^4`
  * `0 <= lists[i].length <= 500`
  * `-10^4 <= lists[i][j] <= 10^4`
  * `lists[i]` 按 **升序** 排列
  * `lists[i].length` 的总和不超过 `10^4`


**Tags:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

**Difficulty:** Hard

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def binsrt(ls,k):
            if not ls or ls[-1][1].val<=k[1].val: 
                ls.append(k)
            else:
                for i in range(len(ls)):
                    if ls[i][1].val>=k[1].val: 
                        ls.insert(i,k)
                        break
            #print('len_ls=%s'%len(ls))

        ls =[e for e in lists if e is not None]        
        if not ls:return None
        if len(ls)==1:return ls[0]
        pls,nls,vls = [(i,ls[i]) for i in range(len(ls))],[],[]
        pls = sorted(pls,key=lambda x:x[1].val)
        #print(pls)
        cnt=1000000
        while cnt and pls:
            cnt-=1
            lsi,nd = pls.pop(0)
            #print('cnt=%s p1=%s lsi=%s'%(cnt,len(pls),lsi))
            if nls:nls[-1].next=nd
            nls.append(nd)
            vls.append(nd.val)
            #print(vls)
            if ls[lsi].next:
                ls[lsi] = ls[lsi].next 
                binsrt(pls,(lsi,ls[lsi]))
            else:
                print('end_nd%s'%lsi)
        return nls[0] 
```

[title]: https://leetcode-cn.com/problems/merge-k-sorted-lists
