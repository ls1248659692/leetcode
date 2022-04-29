# [Top K Frequent Elements][title]

## Description

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

**示例 1:**
            **输入:** nums = [1,1,1,2,2,3], k = 2    **输出:** [1,2]    

**示例 2:**
            **输入:** nums = [1], k = 1    **输出:** [1]

**提示：**

  * `1 <= nums.length <= 105`
  * `k` 的取值范围是 `[1, 数组中不相同的元素的个数]`
  * 题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的

**进阶：** 你所设计算法的时间复杂度 **必须** 优于 `O(n log n)` ，其中 `n` __ 是数组大小。


**Tags:** Array, Hash Table, Divide and Conquer, Bucket Sort, Counting, Quickselect, Sorting, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        # print( cnt.most_common(k))
        return [e[0] for e in cnt.most_common(k)]
```

[title]: https://leetcode-cn.com/problems/top-k-frequent-elements
