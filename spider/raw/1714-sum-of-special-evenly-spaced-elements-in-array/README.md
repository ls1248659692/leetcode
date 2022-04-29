# [Sum Of Special Evenly-Spaced Elements In Array][title]

## Description

给定一个 **索引从 0 开始** 的整数类型数组 `nums` ，包含 `n` 个非负整数。

另外给定一个（包含查询指令的）数组 `queries` ，其中 `queries[i] = [xi, yi]`。 第 `i` 个查询指令的答案是
`nums[j]` 中满足该条件的所有元素的和： `xi <= j < n` 且 `(j - xi)` 能被 `yi` 整除。

返回一个数组 __`answer`，其中 __`answer.length == queries.length` 且 `answer[i]` 是第 `i`
个查询指令的答案对 `109 + 7` 取模。

**示例 1:**
            **输入:** nums = [0,1,2,3,4,5,6,7], queries = [[0,3],[5,1],[4,2]]    **输出:** [9,18,10]    **解释:** 每次查询的答案如下：    1) 符合查询条件的索引 j 有 0、 3 和 6。 nums[0] + nums[3] + nums[6] = 9    2) 符合查询条件的索引 j 有 5、 6 和 7。 nums[5] + nums[6] + nums[7] = 18    3) 符合查询条件的索引 j 有 4 和 6。 nums[4] + nums[6] = 10    

**示例 2:**
            **输入:** nums = [100,200,101,201,102,202,103,203], queries = [[0,7]]    **输出:** [303]    

**提示：**

  * `n == nums.length`
  * `1 <= n <= 5 * 104`
  * `0 <= nums[i] <= 109`
  * `1 <= queries.length <= 1.5 * 105`
  * `0 <= xi < n`
  * `1 <= yi <= 5 * 104`


**Tags:** Array, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/sum-of-special-evenly-spaced-elements-in-array
