# [Boats to Save People][title]

## Description

给定数组 `people` 。`people[i]`表示第 `i` 个人的体重 ， **船的数量不限** ，每艘船可以承载的最大重量为 `limit`。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 `limit`。

返回 _承载所有人所需的最小船数_  。



**示例 1：**
            **输入：** people = [1,2], limit = 3    **输出：** 1    **解释：** 1 艘船载 (1, 2)    

**示例 2：**
            **输入：** people = [3,2,2,1], limit = 3    **输出：** 3    **解释：** 3 艘船分别载 (1, 2), (2) 和 (3)    

**示例 3：**
            **输入：** people = [3,5,3,4], limit = 5    **输出：** 4    **解释：** 4 艘船分别载 (3), (3), (4), (5)



**提示：**

  * `1 <= people.length <= 5 * 104`
  * `1 <= people[i] <= limit <= 3 * 104`


**Tags:** Greedy, Array, Two Pointers, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/boats-to-save-people
