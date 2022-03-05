# [Split Linked List in Parts][title]

## Description

给你一个头结点为 `head` 的单链表和一个整数 `k` ，请你设计一个算法将链表分隔为 `k` 个连续的部分。

每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。

这 `k` 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。

返回一个由上述 `k` 部分组成的数组。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg)
            **输入：** head = [1,2,3], k = 5    **输出：** [[1],[2],[3],[],[]]    **解释：**    第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。    最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg)
            **输入：** head = [1,2,3,4,5,6,7,8,9,10], k = 3    **输出：** [[1,2,3,4],[5,6,7],[8,9,10]]    **解释：**    输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。    



**提示：**

  * 链表中节点的数目在范围 `[0, 1000]`
  * `0 <= Node.val <= 1000`
  * `1 <= k <= 50`


**Tags:** Linked List

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head) 
        base=len(tls)//k 
        lft=len(tls)-base*k     
        print(base,lft)
        nls=[]
        i=0
        while i<len(tls):
            lent = base+1 if len(nls)<lft else base
            print('i=%slent=%s'%(i,lent))
            nls.append(tls[i])
            if i+lent-1<len(tls):tls[i+lent-1].next=None
            i += lent
        while len(nls)<k: nls.append(None)
        return nls
```

[title]: https://leetcode-cn.com/problems/split-linked-list-in-parts
