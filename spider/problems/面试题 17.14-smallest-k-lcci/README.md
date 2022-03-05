# [Smallest K LCCI][title]

## Description

设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

**示例：**
            **输入：** arr = [1,3,5,7,2,4,6,8], k = 4    **输出：** [1,2,3,4]    

**提示：**

  * `0 <= len(arr) <= 100000`
  * `0 <= k <= min(100000, len(arr))`


**Tags:** Array, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]
```

[title]: https://leetcode-cn.com/problems/smallest-k-lcci
