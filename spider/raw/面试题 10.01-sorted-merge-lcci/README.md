# [Sorted Merge LCCI][title]

## Description

给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为  _m_ 和 _n_ 。

**示例:**
            **输入:**    A = [1,2,3,0,0,0], m = 3    B = [2,5,6],       n = 3        **输出:**  [1,2,2,3,5,6]

**说明:**

  * `A.length == n + m`


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        #ta=None
        #return ta is None

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if B[j] is None :continue
                if A[i]<B[j]:
                    A[i+j+1]=B[j]
                    B[j]=None
                else:
                    A[i+j+1]=A[i]
                    #A[i]=-1
                    break
        for j in range(n-1,-1,-1):
            if B[j] is not None:A[j]=B[j]
        return A

```

[title]: https://leetcode-cn.com/problems/sorted-merge-lcci
