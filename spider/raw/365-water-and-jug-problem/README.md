# [Water and Jug Problem][title]

## Description

有两个水壶，容量分别为 `jug1Capacity` 和 `jug2Capacity` 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到
`targetCapacity` 升。

如果可以得到 `targetCapacity` 升水，最后请用以上水壶中的一或两个来盛放取得的 `targetCapacity` 升水。

你可以：

  * 装满任意一个水壶
  * 清空任意一个水壶
  * 从一个水壶向另外一个水壶倒水，直到装满或者倒空



**示例 1:**              **输入:** jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4    **输出:** true    **解释** ：来自著名的 [ _"Die Hard"_](https://www.youtube.com/watch?v=BVtQNK_ZUJg)

**示例 2:**
            **输入:** jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5    **输出:** false    

**示例 3:**
            **输入:** jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3    **输出:** true    



**提示:**

  * `1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106`


**Tags:** Depth-First Search, Breadth-First Search, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/water-and-jug-problem
