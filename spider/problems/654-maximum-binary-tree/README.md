# [Maximum Binary Tree][title]

## Description

给定一个不重复的整数数组 `nums` 。  **最大二叉树**  可以用下面的算法从 `nums` 递归地构建:

  1. 创建一个根节点，其值为 `nums` 中的最大值。
  2. 递归地在最大值  **左边**  的  **子数组前缀上**  构建左子树。
  3. 递归地在最大值 **右边** 的  **子数组后缀上**  构建右子树。

返回  _`nums` 构建的 _**_最大二叉树_ **。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg)
            **输入：** nums = [3,2,1,6,0,5]    **输出：** [6,3,5,null,2,0,null,null,1]    **解释：** 递归调用如下所示：    - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。        - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。            - 空数组，无子节点。            - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。                - 空数组，无子节点。                - 只有一个元素，所以子节点是一个值为 1 的节点。        - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。            - 只有一个元素，所以子节点是一个值为 0 的节点。            - 空数组，无子节点。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg)
            **输入：** nums = [3,2,1]    **输出：** [3,null,2,null,1]    



**提示：**

  * `1 <= nums.length <= 1000`
  * `0 <= nums[i] <= 1000`
  * `nums` 中的所有整数 **互不相同**


**Tags:** Stack, Tree, Array, Divide and Conquer, Binary Tree, Monotonic Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-binary-tree
