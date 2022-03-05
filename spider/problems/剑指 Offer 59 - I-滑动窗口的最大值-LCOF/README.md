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

``` python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        if len(nums) < k:
            return nums
        for i in range(0,len(nums)):
            if len(nums[i:i+k]) == k:
                list1.append(max(nums[i:i+k]))
        return list1

        def calc_mxi(b,e):
            mxli = [e-1]
            for i in range(e-2,b-1,-1):
                if ns[i]>ns[mxli[0]]:
                    mxli.insert(0,i)
            return mxli       

```

[title]: https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
