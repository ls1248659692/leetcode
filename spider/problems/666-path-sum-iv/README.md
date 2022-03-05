# [Path Sum IV][title]

## Description

对于一棵深度小于 `5` 的树，可以用一组三位十进制整数来表示。对于每个整数：

  * 百位上的数字表示这个节点的深度 `d`，`1 <= d <= 4`。
  * 十位上的数字表示这个节点在当前层所在的位置 `P`， `1 <= p <= 8`。位置编号与一棵满二叉树的位置编号相同。
  * 个位上的数字表示这个节点的权值 `v`，`0 <= v <= 9`。

给定一个包含三位整数的  **升序  **数组 `nums` ，表示一棵深度小于 `5` 的二叉树，请你返回 _从根到所有叶子结点的路径之和  _。

**保证  **给定的数组表示一个有效的连接二叉树。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/30/pathsum4-1-tree.jpg)
            **输入:** nums = [113, 215, 221]    **输出:** 12    **解释:** 列表所表示的树如上所示。    路径和 = (3 + 5) + (3 + 1) = 12.    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/04/30/pathsum4-2-tree.jpg)
            **输入:** nums = [113, 221]    **输出:** 4    **解释:** 列表所表示的树如上所示。    路径和 = (3 + 1) = 4.    



**提示:**

  * `1 <= nums.length <= 15`
  * `110 <= nums[i] <= 489`
  * `nums` 表示深度小于 `5` 的有效二叉树


**Tags:** Tree, Depth-First Search, Array, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/path-sum-iv
