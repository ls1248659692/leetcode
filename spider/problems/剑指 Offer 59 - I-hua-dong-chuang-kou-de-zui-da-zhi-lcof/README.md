# [滑动窗口的最大值 LCOF][title]

## Description

给定一个数组 `nums` 和滑动窗口的大小 `k`，请找出所有滑动窗口里的最大值。

**示例:**
            **输入:** _nums_ = [1,3,-1,-3,5,3,6,7], 和 _k_ = 3    **输出:**[3,3,5,5,6,7]     **解释:**      滑动窗口的位置                最大值    ---------------               -----    [1  3  -1] -3  5  3  6  7       3     1 [3  -1  -3] 5  3  6  7       3     1  3 [-1  -3  5] 3  6  7       5     1  3  -1 [-3  5  3] 6  7       5     1  3  -1  -3 [5  3  6] 7       6     1  3  -1  -3  5 [3  6  7]      7



**提示：**

你可以假设 _k_ 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：<https://leetcode-cn.com/problems/sliding-window-maximum/>


**Tags:** Queue, Sliding Window, Monotonic Queue, Heap (Priority Queue)

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
