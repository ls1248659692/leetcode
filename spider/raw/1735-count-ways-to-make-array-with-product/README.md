# [Count Ways to Make Array With Product][title]

## Description

给你一个二维整数数组 `queries` ，其中 `queries[i] = [ni, ki]` 。第 `i` 个查询 `queries[i]`
要求构造长度为 `ni` 、每个元素都是正整数的数组，且满足所有元素的乘积为 `ki` ，请你找出有多少种可行的方案。由于答案可能会很大，方案数需要对
`109 + 7` **取余** 。

请你返回一个整数数组 __`answer`，满足 __`answer.length == queries.length` ，其中
__`answer[i]`是第 __`i` 个查询的结果。

**示例 1：**
            **输入：** queries = [[2,6],[5,1],[73,660]]    **输出：** [4,1,50734910]    **解释：** 每个查询之间彼此独立。    [2,6]：总共有 4 种方案得到长度为 2 且乘积为 6 的数组：[1,6]，[2,3]，[3,2]，[6,1]。    [5,1]：总共有 1 种方案得到长度为 5 且乘积为 1 的数组：[1,1,1,1,1]。    [73,660]：总共有 1050734917 种方案得到长度为 73 且乘积为 660 的数组。1050734917 对 109 + 7 取余得到 50734910 。    

**示例 2 ：**
            **输入：** queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]    **输出：** [1,2,3,10,5]    

**提示：**

  * `1 <= queries.length <= 104 `
  * `1 <= ni, ki <= 104`


**Tags:** Array, Math, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/count-ways-to-make-array-with-product
