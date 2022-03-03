# [Sliding Window Maximum][title]

## Description

给你一个整数数组 `nums`，有一个大小为 `k` _ _ 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k`
个数字。滑动窗口每次只向右移动一位。

返回 _滑动窗口中的最大值_ 。



**示例 1：**
            **输入：** nums = [1,3,-1,-3,5,3,6,7], k = 3    **输出：** [3,3,5,5,6,7]    **解释：**    滑动窗口的位置                最大值    ---------------               -----    [1  3  -1] -3  5  3  6  7       **3**     1 [3  -1  -3] 5  3  6  7       **3**     1  3 [-1  -3  5] 3  6  7      **5**     1  3  -1 [-3  5  3] 6  7       **5**     1  3  -1  -3 [5  3  6] 7       **6**     1  3  -1  -3  5 [3  6  7]      **7**    

**示例 2：**
            **输入：** nums = [1], k = 1    **输出：** [1]    



**提示：**

  * `1 <= nums.length <= 105`
  * `-104 <= nums[i] <= 104`
  * `1 <= k <= nums.length`


**Tags:** Queue, Array, Sliding Window, Monotonic Queue, Heap (Priority Queue)

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/sliding-window-maximum
