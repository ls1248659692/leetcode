# [Nested List Weight Sum II][title]

## Description

给你一个整数嵌套列表 `nestedList` ，每一个元素要么是一个整数，要么是一个列表（这个列表中的每个元素也同样是整数或列表）。

整数的 **深度** 取决于它位于多少个列表内部。例如，嵌套列表 `[1,[2,2],[[3],2],1]` 的每个整数的值都等于它的 **深度** 。令
`maxDepth` 是任意整数的 **最大深度** 。

整数的 **权重** 为 `maxDepth - (整数的深度) + 1` 。

将 `nestedList` 列表中每个整数先乘权重再求和，返回该加权和。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex1.png)
            **输入：** nestedList = [[1,1],2,[1,1]]    **输出：** 8    **解释：** 4 **** 个 1 在深度为 1 的位置， 一个 2 在深度为 2 的位置。    1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex2.png)
            **输入：** nestedList = [1,[4,[6]]]    **输出：** 17    **解释：** 一个 1 在深度为 3 的位置， 一个 4 在深度为 2 的位置，一个 6 在深度为 1 的位置。     1*3 + 4*2 + 6*1 = 17    



**提示：**

  * `1 <= nestedList.length <= 50`
  * 嵌套列表中整数的值在范围 `[-100, 100]`
  * 任意整数的最大 **深度** 小于等于 `50`


**Tags:** Stack, Depth-First Search, Breadth-First Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/nested-list-weight-sum-ii
