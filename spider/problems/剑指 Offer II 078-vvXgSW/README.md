# [合并排序链表][title]

## Description

给定一个链表数组，每个链表都已经按升序排列。

请将所有链表合并到一个升序链表中，返回合并后的链表。



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



注意：本题与主站 23 题相同： <https://leetcode-cn.com/problems/merge-k-sorted-lists/>


**Tags:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/vvXgSW
