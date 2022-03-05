# [Median of Two Sorted Arrays][title]

## Description

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。



**示例 1：**
            **输入：** nums1 = [1,3], nums2 = [2]    **输出：** 2.00000    **解释：** 合并数组 = [1,2,3] ，中位数 2    

**示例 2：**
            **输入：** nums1 = [1,2], nums2 = [3,4]    **输出：** 2.50000    **解释：** 合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5    





**提示：**

  * `nums1.length == m`
  * `nums2.length == n`
  * `0 <= m <= 1000`
  * `0 <= n <= 1000`
  * `1 <= m + n <= 2000`
  * `-106 <= nums1[i], nums2[i] <= 106`


**Tags:** Array, Binary Search, Divide and Conquer

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #n = sorted(nums1+nums2)
        #return n[len(n)//2] if len(n)%2==1 else (n[len(n)//2]+n[len(n)//2-1])/2
        def v1():
            ln1,ln2,n1,n2= (len(nums2),len(nums1),nums2,nums1) if len(nums1)<len(nums2) else (len(nums1),len(nums2),nums1,nums2)
            for i in range(ln2//2):
                if n2[i-1]<n1[(ln1+ln2)//2-i]<n2[i]: return f(n2[i],n1[(ln1+ln2)//2-i])
                
        def v2():
            while len(n1) and len(n2):
                mx,mi=max(n1[0],n1[-1],n2[0],n2[-1]),min(n1[0],n1[-1],n2[0],n2[-1])
                n1.remove(mx),n1.remove(mi)
            return n1[len(n1)//2] if n1 else 0

        def v3(nums1,nums2):
            mm = len(nums1) + len(nums2)
            comb_nums = [nums1.pop() if (nums1 and nums2 and nums1[-1] >= nums2[-1]) or not nums2 else nums2.pop() for ii in range(mm // 2 + 1)]
            return ((comb_nums[-2] + comb_nums[-1]) / 2) if mm % 2 == 0 else comb_nums[-1]

        return v3(nums1,nums2)
```

[title]: https://leetcode-cn.com/problems/median-of-two-sorted-arrays
