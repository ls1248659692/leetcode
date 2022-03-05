# [Merge Sorted Array][title]

## Description

给你两个按 **非递减顺序** 排列的整数数组 `nums1` __ 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和
`nums2` 中的元素数目。

请你 **合并** `nums2` __ 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意：** 最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前
`m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。



**示例 1：**
            **输入：** nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3    **输出：** [1,2,2,3,5,6]    **解释：** 需要合并 [1,2,3] 和 [2,5,6] 。    合并结果是 [ _ **1**_ , _ **2**_ ,2, _ **3**_ ,5,6] ，其中斜体加粗标注的为 nums1 中的元素。    

**示例 2：**
            **输入：** nums1 = [1], m = 1, nums2 = [], n = 0    **输出：** [1]    **解释：** 需要合并 [1] 和 [] 。    合并结果是 [1] 。    

**示例 3：**
            **输入：** nums1 = [0], m = 0, nums2 = [1], n = 1    **输出：** [1]    **解释：** 需要合并的数组是 [] 和 [1] 。    合并结果是 [1] 。    注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。    



**提示：**

  * `nums1.length == m + n`
  * `nums2.length == n`
  * `0 <= m, n <= 200`
  * `1 <= m + n <= 200`
  * `-109 <= nums1[i], nums2[j] <= 109`



**进阶：** 你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_ii=0
        for nn in range(len(nums2)):
            n2=nums2[nn]
            #print('check_n2=%d'%n2)
            append=False
            for ii in range(last_ii,m+n):
                if n2<=nums1[ii]:
                    for jj in range(m+nn-1,ii-1,-1):
                        nums1[jj+1]=nums1[jj]
                    nums1[ii]=n2
                    last_ii =ii
                    #print(nums1)
                    break
                elif ii>=m+nn:
                    append=True
                    break
                else:
                    continue
            if append:
                nums1[nn-n]=n2
```

[title]: https://leetcode-cn.com/problems/merge-sorted-array
