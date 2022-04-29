# [Minimum Cost to Move Chips to The Same Position][title]

## Description

有 `n` 个筹码。第 `i` 个芯片的位置是 `position[i]` 。

我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 `i` 个芯片的位置从 `position[i]` 改变为:

  * `position[i] + 2` 或 `position[i] - 2` ，此时 `cost = 0`
  * `position[i] + 1` 或 `position[i] - 1` ，此时 `cost = 1`

返回将所有筹码移动到同一位置上所需要的 _最小代价_ 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg)
            **输入：** position = [1,2,3]    **输出：** 1    **解释：** 第一步:将位置3的芯片移动到位置1，成本为0。    第二步:将位置2的芯片移动到位置1，成本= 1。    总成本是1。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg)
            **输入：** position = [2,2,2,3,3]    **输出：** 2    **解释：** 我们可以把位置3的两个芯片移到位置2。每一步的成本为1。总成本= 2。    

**示例 3:**
            **输入：** position = [1,1000000000]    **输出：** 1    



**提示：**

  * `1 <= chips.length <= 100`
  * `1 <= chips[i] <= 10^9`


**Tags:** Greedy, Array, Math

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position
